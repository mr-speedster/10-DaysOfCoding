#include<stdio.h>
void findWaitingTime(int n,int process[],int bt[],int wt[])
{
    int i;
    wt[0]=1;
    for ( i = 0; i < n; i++)
    {
        wt[i+1]=bt[i]+wt[i];
    }   
}
void findTurnAroundTime(int n,int process[],int bt[],int wt[],int tat[])
{
    int i;
    for ( i = 0; i < n; i++)
    {
        tat[i]=wt[i]+bt[i];
    }  
}
void findAverageTime(int process[],int n,int bt[])
{
    int wt[n],tat[n],total_wt=0,total_tat=0;
    findWaitingTime(n,process,bt,wt);
    findTurnAroundTime(n,process,bt,wt,tat);
    printf("process\tBT\twt\ttat\t");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t",process[i]);
        printf("%d\t",bt[i]);
        printf("%d\t",wt[i]);
        printf("%d\t",tat[i]);
        total_tat=total_tat+tat[i];
        total_wt=total_wt+wt[i];
    }
    printf("avg=%d",total_wt/n);
    printf("avg=%d",total_tat);
}
int main()
{
    int n;
    printf("enter the number of processes");
    scanf("%d",&n);
    int process[n],bt[n];
    printf("Enter the processes");
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&process[i]);
    }
    printf("Enter the burst time for each process");
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&bt[i]);
    }
    findAverageTime(process,n,bt);
}