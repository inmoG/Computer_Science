
#include <stdio.h>
int main(void) {
  int a = 10, b = 15, total;
  double avg;
  int *pa, *pb;
  int *pt = &total;
  double *pg = &avg;

  pa = &a; // a의 주소에는 값 10이 있다.
  pb = &b; // b의 주소에는 값 15가 있다.

  *pt = *pa + *pb;
  *pg = *pt / 2.0;

  printf("두 정수의 값 : %d, %d\n", *pa, *pb);
  printf("두 정수의 합 : %d\n", *pt); // pt는 total의 주소를 가리킨다.
  printf("두 정수의 합2 : %d\n", total);
  printf("두 정수의 평균 : %.1lf\n", *pg); // pg는 avg의 주소를 가리킨다.
  printf("두 정수의 평균2 : %.1lf\n", avg);

  return 0;
}