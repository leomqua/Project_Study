#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void menu(int *nivel, int *dificuldade) {
    printf("Escolha o nível de dificuldade:\n");
    scanf("%d", nivel);
    while (*nivel < 1 || *nivel > 7) {
        printf("Só existe o nível de 1 - 7\n");
        printf("Digite outro número novamente: ");
        scanf("%d", nivel);
    }
    printf("Escolha o problema aritmético para estudar:");
    printf("\n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Mistura de todos juntos\n");
    scanf("%d", dificuldade);
    while (*dificuldade < 1 || *dificuldade > 5) {
        printf("Só existe a dificuldade de 1 - 5\n");
        printf("Digite outro número novamente: ");
        scanf("%d", dificuldade);
    }
}

int soma(int a, int add) {
    return a + add;
}

int sub(int a, int subt) {
    return a - subt;
}

int mult(int a, int multi) {
    return a * multi;
}

float dive(int a, int divisor) {
    return (float)a / divisor;
}

void operação(int nivel, int dificuldade) {
    int casa, casas, i = 0, respostas_corretas = 0;
    char input[10];
    float resposta, resposta_float;

    srand(time(NULL));

    for (i = 0; i < 11; i++) {
        casa = rand() % (nivel == 1 ? 10 : (nivel == 2 ? 100 : (nivel == 3 ? 1000 : (nivel == 4 ? 10000 : (nivel == 5 ? 100000 : (nivel == 6 ? 1000000 : 10000000))))));
        casas = rand() % (nivel == 1 ? 10 : (nivel == 2 ? 100 : (nivel == 3 ? 1000 : (nivel == 4 ? 10000 : (nivel == 5 ? 100000 : (nivel == 6 ? 1000000 : 10000000))))));

        if (dificuldade == 1) {
            printf("Quanto é %d somado com %d? (ou digite 'q' para sair): ", casa, casas);
            scanf("%s", input);
            if (input[0] == 'q') {
                printf("Você escolheu sair. Até a próxima!\n");
                return;
            }
            resposta = atoi(input);
            if (resposta == soma(casa, casas)) {
                printf("Muito bem!\n");
                respostas_corretas++;
            } else {
                printf("Não. Continue tentando.\n");
            }
        } else if (dificuldade == 2) {
            printf("Quanto é %d subtraído por %d? (ou digite 'q' para sair): ", casa, casas);
            scanf("%s", input);
            if (input[0] == 'q') {
                printf("Você escolheu sair. Até a próxima!\n");
                return;
            }
            resposta = atoi(input);
            if (resposta == sub(casa, casas)) {
                printf("Muito bem!\n");
                respostas_corretas++;
            } else {
                printf("Não. Continue tentando.\n");
            }
        } else if (dificuldade == 3) {
            printf("Quanto é %d multiplicado por %d? (ou digite 'q' para sair): ", casa, casas);
            scanf("%s", input);
            if (input[0] == 'q') {
                printf("Você escolheu sair. Até a próxima!\n");
                return;
            }
            resposta = atoi(input);
            if (resposta == mult(casa, casas)) {
                printf("Muito bem!\n");
                respostas_corretas++;
            } else {
                printf("Não. Continue tentando.\n");
            }
        } else if (dificuldade == 4) {
            printf("Quanto é %d dividido por %d? (ou digite 'q' para sair): ", casa, casas);
            scanf("%s", input);
            if (input[0] == 'q') {
                printf("Você escolheu sair. Até a próxima!\n");
                return;
            }
            resposta_float = atof(input);
            if (resposta_float == dive(casa, casas)) {
                printf("Muito bem!\n");
                respostas_corretas++;
            } else {
                printf("Não. Continue tentando.\n");
            }
        }

        if (dificuldade == 5) {
            for (int j = 0; j < 3; j++) {
                printf("Quanto é %d somado com %d? (ou digite 'q' para sair): ", casa, casas);
                scanf("%s", input);
                if (input[0] == 'q') {
                    printf("Você escolheu sair. Até a próxima!\n");
                    return;
                }
                resposta = atoi(input);
                if (resposta == soma(casa, casas)) {
                    printf("Muito bem!\n");
                    respostas_corretas++;
                } else {
                    printf("Não. Continue tentando.\n");
                }
            }
            for (int j = 0; j < 2; j++) {
                printf("Quanto é %d subtraído por %d? (ou digite 'q' para sair): ", casa, casas);
                scanf("%s", input);
                if (input[0] == 'q') {
                    printf("Você escolheu sair. Até a próxima!\n");
                    return;
                }
                resposta = atoi(input);
                if (resposta == sub(casa, casas)) {
                    printf("Muito bem!\n");
                    respostas_corretas++;
                } else {
                    printf("Não. Continue tentando.\n");
                }
            }
            for (int j = 0; j < 2; j++) {
                printf("Quanto é %d multiplicado por %d? (ou digite 'q' para sair): ", casa, casas);
                scanf("%s", input);
                if (input[0] == 'q') {
                    printf("Você escolheu sair. Até a próxima!\n");
                    return;
                }
                resposta = atoi(input);
                if (resposta == mult(casa, casas)) {
                    printf("Muito bem!\n");
                    respostas_corretas++;
                } else {
                    printf("Não. Continue tentando.\n");
                }
            }
            for (int j = 0; j < 3; j++) {
                printf("Quanto é %d dividido por %d? (ou digite 'q' para sair): ", casa, casas);
                scanf("%s", input);
                if (input[0] == 'q') {
                    printf("Você escolheu sair. Até a próxima!\n");
                    return;
                }
                resposta_float = atof(input);
                if (resposta_float == dive(casa, casas)) {
                    printf("Muito bem!\n");
                    respostas_corretas++;
                } else {
                    printf("Não. Continue tentando.\n");
                }
            }
        }
    }

    if (respostas_corretas >= 8) {
        printf("Parabéns, você está pronto para ir para o próximo nível!\n");
    } else {
        printf("Peça ajuda extra ao seu professor\n");
    }
}

void msgcerta() {
    int respostacerta = rand() % 4;
    switch (respostacerta) {
        case 0:
            printf("Muito bem!\n");
            break;
        case 1:
            printf("Excelente!\n");
            break;
        case 2:
            printf("Bom trabalho!\n");
            break;
        case 3:
            printf("Mantenha o bom trabalho!\n");
            break;
    }
}

void msgerrada() {
    int respostaerrada = rand() % 4;
    switch (respostaerrada) {
        case 0:
            printf("Não. Por favor, tente novamente.\n");
            break;
        case 1:
            printf("Errado. Tente mais uma vez.\n");
            break;
        case 2:
            printf("Não desista!\n");
            break;
        case 3:
            printf("Não. Continue tentando.\n");
            break;
    }
}

int main() {
    int nivel, dificuldade;

    srand(time(NULL));
    menu(&nivel, &dificuldade);
    operação(nivel, dificuldade);

    return 0;
}
