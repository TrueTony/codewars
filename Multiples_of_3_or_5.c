int solution(number) 
{
    int i;
    int res;

    i = 0;
    res = 0;
    while (i < number)
    {
        if ((i % 3 == 0) || (i % 5 == 0))
            res += i;
        i++;
    }
    return res;
}

int main(void) 
{
    solution(10);
    return (0);
}
