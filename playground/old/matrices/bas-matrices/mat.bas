Attribute VB_Name = "Mat"
Option Explicit
'Ubound devuelve el �ndice superior de una matriz
'Lbound devuelve el �ndice inferior de una matriz
'**************************************

'Quita una fila y una columna a una matriz de 2 dimensiones
'recuerda los valores
Function Reducir(ByRef MatXY As Variant) As Variant
    Dim Aux As Variant
    'redim altera el tama�o de una matriz
    ReDim Aux(LBound(MatXY) To UBound(MatXY) - 1, LBound(MatXY) To UBound(MatXY) - 1) As Variant
    Dim i As Integer
    Dim J As Integer
    For i = LBound(MatXY) To UBound(MatXY) - 1
        For J = LBound(MatXY) To UBound(MatXY) - 1
            'copia los elementos
            Aux(i, J) = MatXY(i, J)
        Next J
    Next i
    Reducir = Aux
End Function

'suma a y b y lo almacena en c LISTO
Function SumaMat(A, B, C) As Boolean
    On Error GoTo etiqueta
    Dim i As Integer
    Dim J As Integer
    Dim filas As Integer
    Dim cols As Integer
    filas = UBound(A, 1)
    cols = UBound(A, 2)
    For i = 1 To filas
        For J = 1 To cols
            C(i, J) = A(i, J) + B(i, J)
        Next J
    Next i
    SumaMat = True
    Exit Function
    etiqueta:
End Function

'resta a - b y lo almacena en c LISTO
Function RestaMat(A, B, C) As Boolean
    On Error GoTo etiqueta
    Dim i As Integer
    Dim J As Integer
    Dim filas As Integer
    Dim cols As Integer
    filas = UBound(A, 1)
    cols = UBound(A, 2)
    For i = 1 To filas
        For J = 1 To cols
            C(i, J) = A(i, J) - B(i, J)
        Next J
    Next i
    RestaMat = True
    Exit Function
    etiqueta:
End Function

'halla el producto a*b y lo almacena en c LISTO
Function ProductoMat(A, B, C) As Boolean
    On Error GoTo etiqueta
    Dim i As Integer
    Dim J As Integer
    Dim k As Integer
    Dim numFilas As Integer
    Dim numCols As Integer
    Dim Sumandos As Integer
    Dim suma As Double
    numFilas = UBound(A, 1)
    numCols = UBound(B, 2)
    Sumandos = UBound(A, 2)
    For i = 1 To numFilas
        For J = 1 To numCols
            suma = 0
            For k = 1 To Sumandos
                suma = suma + A(i, k) * B(k, J)
            Next k
            C(i, J) = suma
        Next J
    Next i
    ProductoMat = True
    Exit Function
    etiqueta:
End Function

'Devuelve la traspuesta de a LISTO
Function TraspuestaMat(ByVal A) As Variant
    Dim i As Integer
    Dim J As Integer
    Dim numFilas As Integer
    Dim numCols As Integer
    'de a
    numFilas = UBound(A, 1)
    numCols = UBound(A, 2)
    Dim Aux As Variant
    'aux es lo contrario
    ReDim Aux(1 To numCols, 1 To numFilas)
    For i = 1 To numFilas
        For J = 1 To numCols
            Aux(J, i) = A(i, J)
        Next J
    Next i
    TraspuestaMat = Aux
End Function

'Devuelve la adjunta de a
'es decir, la matriz donde cada elemento es el cofactor
'que corresponde a su posici�n LISTO
Function AdjuntaMat(ByVal A) As Variant
    Dim i As Integer
    Dim J As Integer
    Dim numFilas As Integer
    Dim numCols As Integer
    'de a
    numFilas = UBound(A, 1)
    numCols = UBound(A, 2)
    'Dim Aux As Variant
    'aux es del mismo tama�o que a
    ReDim Aux(1 To numFilas, 1 To numCols)
    For i = 1 To numFilas
        For J = 1 To numCols
            Aux(i, J) = Cofactor(A, i, J)
        Next J
    Next i
    AdjuntaMat = Aux
End Function

'Devuelve el cofactor del elemento indicado de la matriz LISTO
Function Cofactor(ByVal Mat, ByVal Fila As Integer, ByVal Col As Integer) As Double
    Dim Signo As Integer
    Dim Aux As Variant
    If UBound(Mat, 1) = 1 Then
        Cofactor = 1
        Exit Function
    End If
    'forma lenta
    'Signo = (-1) ^ (Fila + Col)
    'forma r�pida
    If (Fila + Col) Mod 2 = 0 Then
        'par
        Signo = 1
    Else
        'impar
        Signo = -1
    End If
    Aux = ReduceMat(Mat, Fila, Col)
    Cofactor = Signo * Determinante(Aux)
End Function

'Devuelve la matriz reducida al quitar la
'fila y la columna especificada LISTO
Function ReduceMat(ByVal Mat, Fila As Integer, Col As Integer) As Variant
    Dim n As Integer
    Dim i As Integer
    Dim J As Integer
    Dim obj As Integer
    Dim Aux As Variant
    n = UBound(Mat, 1)
    Aux = Mat
    'corre las filas, se traga la fila especificada
    obj = Fila + 1
    For i = obj To n
        For J = 1 To n
            Aux(i - 1, J) = Aux(i, J)
        Next J
    Next i
    'corre las columnas, se traga la columna especificada
    obj = Col + 1
    For J = obj To n
        For i = 1 To n
            Aux(i, J - 1) = Aux(i, J)
        Next i
    Next J
    'elimina la �ltima fila y columna
    Aux = Reducir(Aux)
    ReduceMat = Aux
End Function

'Devuelve el determinante de una matriz
Function Determinante(ByVal Mat) As Double
    Dim n As Integer
    Dim J As Integer
    Dim suma As Double
    n = UBound(Mat, 2)
    If n = 1 Then
        Determinante = Mat(1, 1)
        Exit Function
    End If
    suma = 0
    Dim cof As Variant
    For J = 1 To n
        'la primera fila
        cof = Cofactor(Mat, 1, J)
        suma = suma + Mat(1, J) * cof
    Next J
    Determinante = suma
End Function

'Devuelve el producto de una matriz por un n�mero real
Function MatxEscalar(ByVal Mat, ByVal Escalar As Double) As Variant
    Dim i As Integer
    Dim J As Integer
    Dim numFilas As Integer
    Dim numCols As Integer
    Dim Aux As Variant
    numFilas = UBound(Mat, 1)
    numCols = UBound(Mat, 2)
    'contiene lo mismo
    If Escalar = 1 Then
        MatxEscalar = Mat
        Exit Function 'el 1 es el m�dulo
    End If
    Aux = Mat
    For i = 1 To numFilas
        For J = 1 To numCols
            Aux(i, J) = Aux(i, J) * Escalar
        Next J
    Next i
    MatxEscalar = Aux
End Function

'Devuelve la inversa de una matriz
'OJO: DEVUELVE "Error" SI LA MATRIZ NO ES INVERTIBLE
Function InversaMat(ByVal A) As Variant
    'recordar:
    'la inversa de a es la adjunta de la traspuesta de a dividida
    'por el determinante de a
    Dim Det As Double
    Dim Adj As Variant
    Dim Tras As Variant
    Det = Determinante(A)
    If Det = 0 Then
        'llamada no v�lida, la matriz no es invertible
        'Err.Raise 5
        InversaMat = "Error"
        Exit Function
    End If
    Tras = TraspuestaMat(A)
    Adj = AdjuntaMat(Tras)
    InversaMat = MatxEscalar(Adj, 1 / Det)
End Function

' Esta rutina obtiene el n�mero de dimensiones de un array
' pasado como argumento, � 0 si no es un array.
Function NumeroDeDim(arr As Variant) As Integer
    Dim dims As Integer, postizo As Long
    On Error Resume Next
    Do
        postizo = UBound(arr, dims + 1)
        If Err Then Exit Do
        dims = dims + 1
    Loop
    NumeroDeDim = dims
End Function

'// Soluci�n de Ecuaciones Lineales
'// Argumentos:
'// A: Arreglo bidimensional que contiene la matriz
'// C: Arreglo unidimensional que entregar� la soluci�n.
Public Static Function Gauss(ByRef A, ByRef C) As Boolean
   
    Dim Tem As Double, Sum As Double, i, l, J, k, n, m
    
    On Error GoTo Gauss_Err
    n = UBound(C)
    m = n + 1
    For l = 1 To n - 1
        J = l
        For k = l + 1 To n
            If (Abs(A(J, l)) >= Abs(A(k, l))) Then
               Else: J = k
            End If
        Next
        If Not (J = l) Then
           For i = 1 To m
               Tem = A(l, i)
               A(l, i) = A(J, i)
               A(J, i) = Tem
           Next
        End If
        For J = l + 1 To n
            Tem = A(J, l) / A(l, l)
            For i = 1 To m
                A(J, i) = A(J, i) - Tem * A(l, i)
            Next
        Next
    Next
    C(n) = A(n, m) / A(n, n)
    For i = 1 To n - 1
        J = n - i
        Sum = 0
        For l = 1 To i
            k = J + l
            Sum = Sum + A(J, k) * C(k)
        Next
        C(J) = (A(J, m) - Sum) / A(J, J)
    Next
    Gauss = True
    Exit Function
    Gauss_Err: Gauss = False
End Function

