//Version 1
//int main(i){for(;i<101;i++){if(i%3==0){printf("Fizz");}if(i%5==0){printf("Buzz");}if(i%3!=0 && i%5!=0){printf("%d",i);}printf("\n");}}

//Version 2
//main(i){for(i=1;i<101;i++){if(i%3==0)printf("Fizz");if(i%5==0)printf("Buzz");if(i%3&&i%5)printf("%d",i);printf("\n");}}

//Version 3
main(i){for(i=1;i<101;i++){printf(i%3?i%5?"%d":"Buzz":"Fizz",i);if(i%15==0)printf("Buzz");printf("\n");}}

