#include <stdio.h>

int main() {
    unsigned char input[] = {0xd4,0x5c,0xdc,0xbb,0x6b,0x1e,0xd3,0x4a,0x4a,0x5e,0xd2,0xdf,0xac,0x7c};
    unsigned char key[] = {0xb2,0x30,0xbd,0xdc,0x10,0x7a,0xe1,0x7b,0x2c,0x3b,0xe2,0xec,0x99,0x01};
    int i;

    for (i = 0; i < 0xe; i = i + 1) {
        input[i] = input[i] ^ key[i];
    }

    // Stampa l'array input
    printf("Array input dopo il loop:\n");
    for (i = 0; i < 0xe; i++) {
        printf("%02x ", input[i]);
    }
    printf("\n");

    // Converti i valori esadecimali in ASCII
    printf("Flag: ");
    for (i = 0; i < 0xe; i++) {
        printf("%c", input[i]);
    }
    printf("\n");

    return 0;
}
