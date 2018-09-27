#include<stdio.h>
#include<stdlib.h>

void singlePrecision();
void doublePrecision();
void singlePrecisionVal(float VAL);

int main(){
  /*PARTE 1.A*/
  //singlePrecision();
  //doublePrecision();

  /*PARTE 1.B*/
  singlePrecisionVal(10.0);
  singlePrecisionVal(17.0);
  singlePrecisionVal(100.0);
  singlePrecisionVal(184.0);
  singlePrecisionVal(1000.0);
  singlePrecisionVal(1575.0);
  singlePrecisionVal(10000.0);
  singlePrecisionVal(17893.0);
  return 0;
}

void singlePrecision(){
  float A = 1.0;
  float s = 2.0;

  while(s > 1.0){
    A = A/2.0;
    s = 1.0 + A;
  }

  printf("The single precision is: %.20f\n", 2*A);
  return;
}

void singlePrecisionVal(float VAL){
  float A = 1.0;
  float s = VAL + A;

  while(s > VAL){
    A = A/2.0;
    s = VAL + A;
  }

  printf("The single precision for VAL: %7.1f is: %.20f\n",VAL, 2*A);
  return;
}


void doublePrecision(){
  double A = 1.0;
  double s = 2.0;

  while(s > 1.0){
    A = A/2.0;
    s = 1.0 + A;
  }

  printf("The double precision is: %.20lf\n", 2*A);
  return;
}
