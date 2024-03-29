# Le pré et la chèvre
# https://edupython.tuxfamily.org/sources/view.php?code=chevre

#   U n e   c h ? v r e   b r o u t e   d e   l ' h e r b e   d a n s   u n   p r ?   c a r r ?   d e   c ? t ?   1 0 m . 
 #   E l l e   e s t   a t t a c h ? e   a u   m i l i e u   d ' u n   c ? t ?   d u   p r ?   p a r   u n e   c o r d e . 
 #   O n   c h e r c h e   ?   c o n n a ? t r e   l ' a i r e   d e   l a   s u r f a c e   d ' h e r b e   d i s p o n i b l e   p o u r   l a   c h ? v r e 
 #   e n   f o n c t i o n   d e   l a   l o n g u e u r   d e   l a   c o r d e . 
 
 x   =   d e m a n d e   ( " L o n g u e u r   d e   l a   c o r d e   ? " )                     #   C e   p r o g r a m m e   e s t   b a s ?   s u r   l e s   f i g u r e s   d e   l a   d o c u m e n t a t i o n   s i t u ? e s 
                                                                                                 #   d a n s   l e   s o u s   p a r a g r a p h e   q u i   c o n c e r n e   l e s   f o n c t i o n s   A r c s i n u s   e t   A r c c o s i n u s 
 i f   x   <   5   : 
                 A i r e   =   p i   *   x   *   x   /   2 
 e l i f   x   <   1 0   : 
         A n g l e A E F   =   a c o s D ( 5   /   x ) 
         A n g l e F E G   =   1 8 0   -   2 * A n g l e A E F 
         A i r e   =   5 * s q r t   ( x * x   -   5 * 5 )   +   p i * x * x / 3 6 0 * A n g l e F E G 
 e l i f   x   <   s q r t   ( 1 2 5 )   : 
         A n g l e M E A   =   a c o s D ( 5   /   x ) 
         A n g l e M E J   =   1 8 0   -   2 * A n g l e M E A 
         A n g l e L E K   =   2   *   a c o s D ( 1 0   /   x ) 
         A n g l e M E L   =   1   /   2   *   ( A n g l e M E J   -   A n g l e L E K ) 
         L K   =   2   *   x   *   s i n D ( a c o s D ( 1 0   /   x ) ) 
         A i r e   =   5 * s q r t ( x * x   -   5 * 5 )   +   p i * x * x /   1 8 0   *   A n g l e M E L   +   5   *   L K 
 e l s e   : 
         A i r e   =   1 0 0                                                                       #   L ' a i r e   v a u t   1 0 0   m ?   c a r   i l   s ' a g i t   a l o r s   d u   p r ?   e n t i e r . 
 p r i n t   ( " L ' a i r e   m e s u r e " ,   A i r e ) 
