#include <iostream>
#include <chrono>
#include <fstream>
#include <string>

using namespace std;
using namespace std::chrono;


float random(float minValue, float maxValue, float stepSize) {
    double min = minValue * (double) (1 / stepSize);
    double max = maxValue * (double) (1 / stepSize);
    double randValue = ((double)rand() / (RAND_MAX + 1) * (max - min) + min);
    return (float) randValue / stepSize;
}

float* generateList(int count) {
    float* testData = new float[count];
    

    return testData;
}



int main()
{
    srand((unsigned)time(0));
    for (int i = 0; i < 20; i++) {
        cout << random(5, 30, 0.0001) << endl;
    }
    auto start = high_resolution_clock::now();

    //-----------------------
    float r = 1;
    for (int i = 1; i < 300000000; i++) {
        r *= i;
        r *= 1 / (float) i;
    }

    //------------------------

    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);

    int time = duration.count();
    //------------------
    ofstream out;
    out.open("result.txt");
    if (out.is_open())
    {
        out << r << endl;
        out << "Time taken by function: " << time << " microseconds" << endl;
    }
    out.close();
    //------------------------
    string line;

    ifstream in("result.txt");
    if (in.is_open())
    {
        while (getline(in, line))
        {
            cout << line << endl;
        }
    }
    in.close();
}

