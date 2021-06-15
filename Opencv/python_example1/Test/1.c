/ create vignetting filter in opencv | opencv创建晕影滤镜
// @mango

#include<iostream>
#include <math.h>
#include <vector>

// opencv4.1
#include<opencv2/opencv.hpp>


// Helper function to calculate the distance between 2 points. | 帮助器函数计算 2 点之间的距离。
double dist(cv::Point a, cv::Point b)
{
    return sqrt(pow((double)(a.x - b.x), 2) + pow((double)(a.y - b.y), 2));
}

// Helper function that computes the longest distance from the edge to the center point. | 帮助器函数,用于计算从边缘到中心点最远的距离。
double getMaxDisFromCorners(const cv::Size& imgSize, const cv::Point& center)
{
    // given a rect and a line | 给定一个矩形和一条线
    // get which corner of rect is farthest from the line | 得到哪个角的矩形是离线最远


    std::vector<cv::Point> corners(4);
    corners[0] = cv::Point(0, 0);
    corners[1] = cv::Point(imgSize.width, 0);
    corners[2] = cv::Point(0, imgSize.height);
    corners[3] = cv::Point(imgSize.width, imgSize.height);

    double max_dis = 0;
    for (int i = 0; i < 4; ++i)
    {
        double dis = dist(corners[i], center);
        if (max_dis < dis)
            max_dis = dis;
    }

    return max_dis;
}

// Helper function that creates a gradient image.  | 帮助函数用于创建一个渐变的图像
// first_point, radius and power, are variables that control the artistic effect of the filter. | first_point,半径和功率是控制滤波器艺术效果的变量。

void generateGradient(cv::Mat& mask)
{
    cv::Point first_point = cv::Point(mask.size().width / 2, mask.size().height / 2);
    double radius = 1.0;
    double power = 0.6;

    // max image radian | 最大图像半径
    double max_image_rad = radius * getMaxDisFromCorners(mask.size(), first_point);

    mask.setTo(cv::Scalar(1));
    for (int i = 0; i < mask.rows; i++)
    {
        for (int j = 0; j < mask.cols; j++)
        {
            double temp = dist(first_point, cv::Point(j, i)) / max_image_rad;
            temp = temp * power;
            double temp_s = pow(cos(temp), 4);
            mask.at<double>(i, j) = temp_s;
        }
    }
}


int main()
{
    std::cout << "OpenCV version : " << CV_VERSION << std::endl;

    cv::Mat img = cv::imread("beach.jpg");
    if (img.empty()) { return -1; }

    // create a mask | 创建一个mask
    cv::Mat mask_img(img.size(), CV_64F);
    generateGradient(mask_img);

    cv::Mat gradient;
    cv::normalize(mask_img, gradient, 0, 255, 32); //cv::normalize(maskImg, gradient, 0, 255, CV_MINMAX);
    cv::imwrite("gradient.png", gradient);

    cv::Mat lab_img(img.size(), CV_8UC3);
    cv::cvtColor(img, lab_img, cv::COLOR_BGR2Lab);

    for (int row = 0; row < lab_img.size().height; row++)
    {
        for (int col = 0; col < lab_img.size().width; col++)
        {
            cv::Vec3b value = lab_img.at<cv::Vec3b>(row, col);
            value.val[0] *= mask_img.at<double>(row, col);
            lab_img.at<cv::Vec3b>(row, col) = value;
        }
    }

    cv::Mat output;
    cv::cvtColor(lab_img, output, cv::COLOR_Lab2BGR);
    cv::imwrite("vignette.png", output);

    std::string window_name = "Vignette-power0.6";
    cv::namedWindow(window_name, cv::WINDOW_NORMAL);
    cv::resizeWindow(window_name, output.size().width / 2, output.size().height / 2);
    cv::imshow(window_name, output);

    cv::waitKey();

    
    return 0;
}
