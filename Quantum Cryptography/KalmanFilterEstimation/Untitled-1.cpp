


i = 0 ;
j = 31;
int variable;
int swapped_variable =0 ;

while ( i < 31 ){

    int temp = 0 ;

    temp =  ( variable & ( 1 << i )  ) >> i  ;
 

        swapped_variable = ( swapped_variable | (temp << j ) );
        j--;
        i++;


    //swapped_variable = ( swapped_variable | ( ( variable & ( 1 << i ) ) << (j) ))
    //i++;
    //j--;
}