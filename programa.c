#include<stdio.h>
#include<math.h>

main(){
    int x = 10, y = 30;
    int z = x + y;
    float w = 4.5;
    printf("Escribe el primer numero:");//esto es un comentario
    scanf("%d", &x);
    printf("Escribe el segundo numero:");
    scanf("%d", &y);
    /*esto es un
    bloquedecomentario*/
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

    for(int i = 0; i < x; i++){
        printf("item: %d", i);
    }
}