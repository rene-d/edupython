# Puissance récursive version 2
# https://edupython.tuxfamily.org/sources/view.php?code=puissV2

# 
 f r o m   l y c e e   i m p o r t   * 
 d e f   p u i s s V 2 ( a , n ) : 
         i f   n = = 1   :                                                     
                 r e t u r n   a 
         e l i f   r e s t e ( n , 2 ) = = 0   : 
                 t e m p = p u i s s V 2 ( a , q u o t i e n t ( n , 2 ) )     
                 r e t u r n   t e m p * t e m p 
         e l s e   : 
                 r e t u r n   a * p u i s s V 2 ( a , n - 1 )             
 
 p r i n t   ( p u i s s V 2 ( 2 , 1 0 ) ) 
 
