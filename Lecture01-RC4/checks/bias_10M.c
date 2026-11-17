#include <stdio.h>
#include <stdint.h>
static uint64_t s=0x9E3779B97F4A7C15ULL;
static uint64_t rnd(void){s^=s<<13;s^=s>>7;s^=s<<17;return s;}
int main(void){
  long N=10000000, c[3]={0,0,0};
  for(long n=0;n<N;n++){
    uint8_t key[16],S[256]; uint64_t a=rnd(),b=rnd();
    for(int k=0;k<8;k++){key[k]=a>>(8*k);key[8+k]=b>>(8*k);}
    for(int i=0;i<256;i++)S[i]=i;
    int j=0; for(int i=0;i<256;i++){j=(j+S[i]+key[i%16])&255;uint8_t t=S[i];S[i]=S[j];S[j]=t;}
    int i=0;j=0; for(int k=0;k<3;k++){i=(i+1)&255;j=(j+S[i])&255;uint8_t t=S[i];S[i]=S[j];S[j]=t;if(S[(S[i]+S[j])&255]==0)c[k]++;}
  }
  for(int k=0;k<3;k++)printf("byte %d: %.3f%%\n",k+1,100.0*c[k]/N);
}
