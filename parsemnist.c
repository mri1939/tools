#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Unpack Binary Sequence to Unsigned Integer 32
*/

unsigned int unpack_uint32(unsigned char *s, int n)
{
    assert(n > 0);
    unsigned int val = 0;
    for (int i = 0, p = n - 1; i < n; i++, p--)
    {
        int r = pow(256, p);
        unsigned int a = (unsigned int)s[i];
        val += r * a;
    }
    return val;
}

/**
 * Parse MNIST Binary file to JSON
 * param filename  : Output Filename
 * param dataname  : Object name in the json
 * param imgfile   : MNIST Image binary file
 * param labelfile : MNIST Label binary file
 * param rev_color : Set the color range from Black(0) to White(255) instead of White(0) to Black(255)
*/


void write_json(const char *filename, const char *dataname, const char *imgfile, const char *labelfile, bool rev_color)
{
    FILE *fpjson = fopen(filename, "w+");
    FILE *fp_img = fopen(imgfile, "r");
    FILE *fp_label = fopen(labelfile, "r");

    unsigned char *int_buff = malloc(4 * sizeof(char));

    // Read File Magic Number
    fread(int_buff, sizeof(char), 4, fp_img);
    unsigned int magic = unpack_uint32(int_buff, 4);
    fread(int_buff, sizeof(char), 4, fp_label);
    unsigned int magic_label = unpack_uint32(int_buff, 4);

    // Read number of images
    fread(int_buff, sizeof(char), 4, fp_img);
    unsigned int num_of_images = unpack_uint32(int_buff, 4);
    fread(int_buff, sizeof(char), 4, fp_label);
    unsigned int num_of_labels = unpack_uint32(int_buff, 4);

    // Read number of images
    fread(int_buff, sizeof(char), 4, fp_img);
    unsigned int rows = unpack_uint32(int_buff, 4);

    // Read number of images
    fread(int_buff, sizeof(char), 4, fp_img);
    unsigned int cols = unpack_uint32(int_buff, 4);
    // Free the int buffer
    free(int_buff);

    // Begin writing process
    fprintf(fpjson, "{\"%s\":[", dataname);

    // Create Byte Pointers for value reading from the file
    unsigned char *pix_val = malloc(sizeof(char));
    unsigned char *label_val = malloc(sizeof(char));
    for (int i = 0; i < num_of_images; i++)
    {
        fread(label_val, sizeof(char), 1, fp_label);
        unsigned int label = unpack_uint32(label_val, 1);
        fprintf(fpjson, "{\"label\":%d,\"img\":[", label);
        for (int j = 0; j < rows; j++)
        {
            fprintf(fpjson, "[");
            for (int k = 0; k < cols; k++)
            {
                fread(pix_val, sizeof(char), 1, fp_img);
                unsigned int pix = unpack_uint32(pix_val, 1);
                if (rev_color)
                {
                    pix = abs(pix-255);
                }
                fprintf(fpjson, "%u", pix);
                if (k != cols - 1)
                {
                    fprintf(fpjson, ",");
                }
            }
            fprintf(fpjson, "]");
            if (j != rows - 1)
            {
                fprintf(fpjson, ",");
            }
        }
        fprintf(fpjson, "]}");
        if (i != num_of_images - 1)
        {
            fprintf(fpjson, ",");
        }
    }
    fprintf(fpjson, "]}");

    // Free, flush, and close
    free(pix_val);
    free(label_val);
    fflush(fpjson);
    fclose(fpjson);
    fclose(fp_img);
    fclose(fp_label);
}

int main(int argc, char **argv)
{
    write_json("train.json", "train", "train-images.idx3-ubyte", "train-labels.idx1-ubyte", false);
    write_json("test.json", "test", "t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte", false);
    write_json("train-reversed.json", "train", "train-images.idx3-ubyte", "train-labels.idx1-ubyte", true);
    write_json("test-reversed.json", "test", "t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte", true);
}
