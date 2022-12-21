
using namespace std;
void insertionSort( int arr[],int n) //arr ---> array of elements , n ---> number of elements
{
    int key, j;            //0    1  2  3  4  5  6
    for (int i=1;i<n;i=++) //80  90|60 30 50 70 40
    {
        key = arr[i]; //60      i=2
        j = i - 1; //1

        while (j>=0 && arr[j]> key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key; //90
    }
}
void printArray(int arr[],int n)
{
    for (int i = 0; i < n; i++)
        cout << aa[i] << " ";
    cout << end1;
}
int main()
{

    int arr[] = { 80, 90, 60, 30, 50, 70, 40 };
    int n = sizeof(arr) / sizeof(arr[0]); //28/

    insertionSort(arr, n);
    printAraay(arr, n);
}