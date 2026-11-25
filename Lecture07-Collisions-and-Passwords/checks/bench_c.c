/* Lecture 7, slides "The cost parameter" and "Task 8: what we saw": bcrypt (libxcrypt, the C library
 * behind crypt(3) on many Linux systems) and SHA-256 (OpenSSL) in C, the same short passwords, one core.
 * A fair comparison: both sides are C code.
 *   gcc -O2 -Wno-deprecated-declarations bench_c.c -o bench_c -lcrypt -lcrypto && ./bench_c
 * 2026-11-25, Intel i5-8265U, quiet, three runs: bcrypt cost 4 about 1 105 per s (0.90 ms), 5: 587 per s, 8: 12.7 ms,
 * 10: 51 ms, 12: 0.20 s; SHA-256 about 5.7 million per s; ratio 5 200 at cost 4, 9 800 at cost 5. */
#include <crypt.h>
#include <openssl/sha.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
int main(void){
  const char *pw[4]={"123456","password","sunshine","iloveyou"};
  struct crypt_data cd; memset(&cd,0,sizeof cd);
  for(int cost=4;cost<=12;cost=(cost==4||cost==5)?cost+1:cost+2){char s[64];snprintf(s,64,"$2b$%02d$Bm9vfEMu3JI4IV.ybN/ip.",cost);
    int n=cost<=8?200:(cost==10?20:5);double t0=now();for(int i=0;i<n;i++)crypt_r(pw[i&3],s,&cd);double t=(now()-t0)/n;
    printf("bcrypt cost %d: %.4f s, %.1f per s\n",cost,t,1/t);}
  unsigned char d[32]; volatile unsigned x=0; long n=20000000; double t0=now();
  for(long i=0;i<n;i++){SHA256_CTX c;SHA256_Init(&c);SHA256_Update(&c,pw[i&3],strlen(pw[i&3]));SHA256_Final(d,&c);x+=d[0];}
  double t=now()-t0; printf("SHA-256: %.0f per s\n",n/t);
  return 0;}
