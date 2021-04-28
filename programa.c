#include<stdio.h>
#include<math.h>

main(){
    int x = 10, y = 30;
    printf("Escribe el primer numero:");//esto es un comentario
    scanf("%d", &x);
    printf("Escribe el segundo numero:");
    scanf("%d", &y);
    /*esto es un
    bloque de comentario*/
    if(x > y){
        printf("El mayor es: %d",x);
    }else{
        if(y > x){
            printf("El mayor es: %d",y);
        }else{
            printf("Son iguales");
        }
    }
    if (x>0 && y>0){
        printf("x e y son mayore que cero");
    }
}