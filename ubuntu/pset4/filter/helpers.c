#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // created nested loop on the array of 1.image height secondary loop of image width
    // for each part of the loop find the average of the RGB Tripple at the image hieght and width and change RGB triple to that
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // find average of colors and set colors to average
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/ 3.0);
            
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //take nested loops of height and width
    //for each part of the loop- apply the sepia formula to the pixel and then set the new sepia (rounded) sepia variables to the color
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            double sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            double sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue; 
            
            if (sepiaRed > 255)
            {
               sepiaRed = 255; 
            }
            
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            
            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
        }
    }
    
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
                temp[j] = image[i][j];
                image[i][j] = image[i][width - 1 - j];
                image[i][width - 1 - j] = temp[j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    // nested loop of height and then width
    // take the average of color values of all of the ones around: i+1, i-1, j+1, j-1 (can this be done with another nested loop inside?)
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // nested loops of the surrounding pixels
            int pixels_counted = 0;
            double redAverage = 0;
            double blueAverage = 0;
            double greenAverage = 0;
            
            for (int k =- 1; k < 2; k++)
            {
                for (int l = - 1; l < 2; l++)
                {
                    if ((i - k) >= 0 && (i - k) < height && (j - l) >= 0 && (j - l) < width)
                    {
                        redAverage += image[i-k][j-l].rgbtRed;
                        blueAverage += image[i-k][j-l].rgbtBlue;
                        greenAverage += image[i-k][j-l].rgbtGreen;
                        pixels_counted ++;
                    }
                }
            }
            
            temp[i][j].rgbtRed = round(redAverage / pixels_counted);
            if (temp[i][j].rgbtRed > 255)
            {
                temp[i][j].rgbtRed = 255;
            }
            
            temp[i][j].rgbtBlue = round(blueAverage / pixels_counted);
            if (temp[i][j].rgbtBlue > 255)
            {
                temp[i][j].rgbtBlue = 255;
            }
            
            temp[i][j].rgbtGreen = round(greenAverage / pixels_counted);
            if (temp[i][j].rgbtGreen > 255)
            {
                temp[i][j].rgbtGreen = 255;
            }
            
        }
        
    }
    
    for (int switchi = 0; switchi < height; switchi++)
    {
        for (int switchj = 0; switchj < width; switchj++)
        {
            image[switchi][switchj].rgbtRed = temp[switchi][switchj].rgbtRed;
            image[switchi][switchj].rgbtGreen = temp[switchi][switchj].rgbtGreen;
            image[switchi][switchj].rgbtBlue = temp[switchi][switchj].rgbtBlue;
        }
    }
    return;
}
