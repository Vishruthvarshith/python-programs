include<iostream.h>
include<conio.h>
class printer
{
    private:
             int a,b,c;
    public:
             void compute()
             void display()
};
class printer::void compute()
{
    cout<<"enter the value of a,b,c"<<endl;
    cin>>a>>b>>c;
    sum=a+b+c;
}
class printer::void display()
{
    cout<<"the sum is" sum<<endl;
}
void main()
{
    printer.obj;
    clscr();
    compute.obj();
    display.obj();
    getch();
};