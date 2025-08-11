Attribute VB_Name = "An�lisis"
Option Explicit

Public Enum Modelo
    Lineal = 1
    Exponecial = 2
    Potencial = 3
    Logar�tmico = 4
    Polin�mico = 5
End Enum
Function Promedio(Vector() As Variant) As Variant
On Error GoTo etiqueta
        Promedio = SumaVector(Vector()) / N�meroElementos(Vector())
    Exit Function
etiqueta:
Promedio = "No disponible"
End Function


Function ErrorT�pico(Vector() As Variant) As Variant
On Error GoTo etiqueta
        ErrorT�pico = Desviaci�nEst�ndar(Vector(), True) / Sqr(N�meroElementos(Vector()) - 1)
    Exit Function
etiqueta:
ErrorT�pico = "No disponible"
End Function

Function MediaGeom�trica(Vector() As Variant) As Variant
On Error GoTo etiqueta
        Dim i As Long
        Dim Productoria As Double
        For i = LBound(Vector()) To UBound(Vector())
            If Vector(i) <= 0 Then GoTo etiqueta
        Next i
        Productoria = 1
        For i = LBound(Vector()) To UBound(Vector())
            Productoria = Productoria * Vector(i)
        Next i
        MediaGeom�trica = Productoria ^ (1 / N�meroElementos(Vector()))
    Exit Function
etiqueta:
MediaGeom�trica = "No disponible"
End Function

Function MediaArm�nica(Vector() As Variant) As Variant
On Error GoTo etiqueta
        Dim SumaInv As Double
        Dim i As Long
        For i = LBound(Vector()) To UBound(Vector())
            If Vector(i) <= 0 Then GoTo etiqueta
        Next i
        SumaInv = 0
        For i = LBound(Vector()) To UBound(Vector())
            SumaInv = SumaInv + (1 / Vector(i))
        Next i
        MediaArm�nica = SumaInv / N�meroElementos(Vector())
        MediaArm�nica = 1 / MediaArm�nica
    Exit Function
etiqueta:
MediaArm�nica = "No disponible"
End Function
Function Moda(Vector() As Variant) As Variant
    On Error GoTo etiqueta
        Dim Repetidos As Long
        Dim i As Long
        Dim j As Long
        Dim contador As Long
        Dim temporal As Double
        Moda = "No disponible"
        contador = 0
        Repetidos = 1
        For i = LBound(Vector()) To UBound(Vector())
            temporal = Vector(i)
            contador = 0
            For j = LBound(Vector()) To UBound(Vector())
                If Vector(j) = temporal Then
                    contador = contador + 1
                End If
            Next j
            If contador > Repetidos Then
                Moda = Vector(i)
                Repetidos = contador
            End If
        Next i
        
    Exit Function
etiqueta:
    Moda = "No disponible"
End Function

Function Mediana(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim Ordenado() As Variant
    Dim n As Long
    n = N�meroElementos(Vector())
    
    If n < 1 Then GoTo etiqueta
    Ordenado() = Vector()
    ShellSortAny Ordenado(), n, False
    If n Mod 2 = 0 Then
        'es par
        Mediana = (Ordenado(n / 2) + Ordenado(1 + n / 2)) / 2
    Else
        'impar
        Mediana = Ordenado((1 + n) / 2)
    End If
    Exit Function
etiqueta:
    Mediana = "No disponible"
End Function

'calcula cualquier cuantil (percentil, decil, cuartil...)
'0 <= k <= 1 de lo contrario devuelve "No disponible"
'n es el n�mero de datos
'Si k no es un m�ltiplo de 1/(n - 1), CUANTIL interpola
'para determinar el valor en el k-�simo cuantil.
'SE REQUIERE la rutina ShellSortAny
Function Cuantil(Vector() As Variant, k As Double) As Variant
On Error GoTo etiqueta
    Dim n As Long
    If k < 0 Or k > 1 Then GoTo etiqueta 'no pierde tiempo
    Dim Ordenado() As Variant 'NO SE ALTERA EL VECTOR ORIGINAL
    Dim r As Integer, s As Double, t As Integer, Pend As Double, Interc As Double
    n = N�meroElementos(Vector())
    If n < 1 Then GoTo etiqueta
    Ordenado() = Vector()
    ShellSortAny Ordenado(), n, False
    s = k * (n - 1) + 1 'posici�n
    'es m�ltiplo, s es una posici�n, es entero
    If s = Int(s) Then
        Cuantil = Ordenado(s)
    'no es m�ltiplo, hay que interpolar
    Else
        r = Int(s) 'el entero menor que s
        t = Ceiling(s)   'el entero mayor que s
        't - r = 1
        Pend = (Ordenado(t) - Ordenado(r)) / (t - r)
        Interc = (Ordenado(r) + Ordenado(t) - Pend * (r + t)) / 2
        Cuantil = Pend * s + Interc
    End If
    Exit Function
etiqueta:
    Cuantil = "No disponible"
End Function

'calcula la interpolaci�n lineal de y para un valor de x dado
Function InterpolaXY(ByVal x As Double, ByVal x1 As Double, ByVal x2 As Double, ByVal y1 As Double, ByVal y2 As Double) As Variant
On Error GoTo etiqueta
    Dim Pend As Double, Interc As Double
    Pend = (y2 - y1) / (x2 - x1)
    Interc = (y1 + y2 - Pend * (x1 + x2)) / 2
    InterpolaXY = Pend * x + Interc
    Exit Function
etiqueta:
    InterpolaXY = "No disponible"
End Function

'calcula los par�metros de la regresi�n polinomial
'devuelve un vector(1 to r+1) con r+1 elementos que
'contiene los coeficientes b, c1, c2, c3, ...cr
'de la ecuaci�n polin�mica y = b + c1x + c2x^2 + c3x^3...+crx^r
'r es el grado deseado del polinomio
'requiere la rutina Gauss, para resolver un sistema lineal
Function PolinomioAjuste(ByVal r As Integer, VectorDependienteY() As Variant, VectorIndependienteX() As Variant) As Variant
On Error GoTo etiqueta
    Dim TermInd() As Variant
    Dim Coef() As Variant
    Dim Sol() As Variant
    Dim Sistema() As Variant
    Dim n As Long
    Dim i As Long
    Dim j As Long
    Dim suma As Double
    Dim contador As Long
    n = N�meroElementos(VectorDependienteY())
    If n < 2 Then GoTo etiqueta 'al menos dos datos
    'define el verdadero grado del polinomio
    If n <= r Then r = n - 1
    'obtiene los t�rminos independientes del sistema
    ReDim TermInd(1 To r + 1, 1 To 1) As Variant
    For j = 0 To r
        suma = 0
        For i = 1 To n
            suma = suma + VectorDependienteY(i) * VectorIndependienteX(i) ^ j
        Next i
        TermInd(j + 1, 1) = suma
    Next j
    'obtiene la matriz de coeficientes del sistema de ecuaciones
    ReDim Coef(1 To r + 1, 1 To r + 1) As Variant
    For i = 0 To r
        For j = 0 To r
            suma = 0
            For contador = 1 To n
                suma = suma + VectorIndependienteX(contador) ^ (i + j)
            Next contador
            Coef(i + 1, j + 1) = suma
        Next j
    Next i
    'resuelve el sistema usando Gauss
    ReDim Sol(1 To r + 1) As Variant
    Sistema = Coef
    ReDim Preserve Sistema(1 To r + 1, 1 To r + 2) As Variant
    For i = 1 To r + 1
        Sistema(i, r + 2) = TermInd(i, 1)
    Next i
    If Not Gauss(Sistema(), Sol()) Then GoTo etiqueta
    PolinomioAjuste = Sol
    Exit Function
etiqueta:
    PolinomioAjuste = "No disponible"
End Function
'ecuaci�n de ajuste polinomial como texto
Function Ecuaci�nPolinomio(ByVal r As Integer, Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim MisCoef As Variant
    Dim i As Long
    Dim n As Long
    n = N�meroElementos(Vector())
    'define el verdadero grado del polinomio
    If n <= r Then r = n - 1
    MisCoef = PolinomioAjuste(r, Vector(), LogEspecial(n, False))
    'para los t�rminos
    Dim Segmento As String
    Dim xpot As String
    For i = r To 0 Step -1
        Select Case i
            Case 0
                xpot = ""
            Case 1
                xpot = "x"
            Case Else
                xpot = "x^" & i
        End Select
        Select Case Sgn(MisCoef(i + 1))
            Case 0
                'no se muestra el t�rmino
                Segmento = ""
            Case 1
                Segmento = IIf(i = r, "", " + ") & Abs(Round(MisCoef(i + 1), 4)) & xpot
            Case -1
                Segmento = " - " & Abs(Round(MisCoef(i + 1), 4)) & xpot
        End Select
        Ecuaci�nPolinomio = Ecuaci�nPolinomio & Segmento
    Next i
    If Ecuaci�nPolinomio = "" Then Ecuaci�nPolinomio = "0"
    Ecuaci�nPolinomio = "y = " & Ecuaci�nPolinomio
    Exit Function
etiqueta:
    Ecuaci�nPolinomio = "No disponible"
End Function

Function RangoIntercuart�lico(Vector() As Variant) As Variant
On Error GoTo etiqueta
    RangoIntercuart�lico = Cuantil(Vector(), 0.75) - Cuantil(Vector(), 0.25)
Exit Function
etiqueta:
    RangoIntercuart�lico = "No disponible"
End Function

Function Min(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim temporal As Double
    Dim i As Long
    temporal = Vector(LBound(Vector()))
    For i = LBound(Vector()) To UBound(Vector())
        If Vector(i) < temporal Then
            temporal = Vector(i)
        End If
    Next i
    Min = temporal
    Exit Function
etiqueta:
    Min = "No disponible"
End Function

Function Max(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim temporal As Double
    Dim i As Long
    temporal = Vector(LBound(Vector()))
    For i = LBound(Vector()) To UBound(Vector())
        If Vector(i) > temporal Then
            temporal = Vector(i)
        End If
    Next i
    Max = temporal
    Exit Function
etiqueta:
    Max = "No disponible"
End Function

Function Desviaci�nEst�ndar(Vector() As Variant, Optional ByVal Poblacional As Boolean = True) As Variant
On Error GoTo etiqueta
    Desviaci�nEst�ndar = Sqr(Varianza(Vector(), Poblacional))
    Exit Function
etiqueta:
    Desviaci�nEst�ndar = "No disponible"
End Function

Function Rango(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Rango = Max(Vector()) - Min(Vector())
    Exit Function
etiqueta:
    Rango = "No disponible"
End Function

Function CoeficienteAsimetr�a(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim n As Long
    Dim i As Long
    Dim suma As Double
    n = N�meroElementos(Vector())
    If n < 3 Then GoTo etiqueta 'al menos 3
    Dim miMedia As Double
    Dim miDesv As Double
    miDesv = Desviaci�nEst�ndar(Vector(), False) 'muestral
    If miDesv = 0 Then GoTo etiqueta
    miMedia = Promedio(Vector())
    suma = 0
    For i = LBound(Vector()) To UBound(Vector())
        suma = suma + ((Vector(i) - miMedia) / miDesv) ^ 3
    Next i
    CoeficienteAsimetr�a = n * suma / ((n - 1) * (n - 2))
    Exit Function
etiqueta:
    CoeficienteAsimetr�a = "No disponible"
End Function

Function Curtosis(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim n As Long
    Dim i As Long
    Dim suma As Double
    n = N�meroElementos(Vector())
    If n < 4 Then GoTo etiqueta 'al menos 4
    Dim miMedia As Double
    Dim miDesv As Double
    miDesv = Desviaci�nEst�ndar(Vector(), False) 'muestral
    If miDesv = 0 Then GoTo etiqueta
    miMedia = Promedio(Vector())
    suma = 0
    For i = LBound(Vector()) To UBound(Vector())
        suma = suma + ((Vector(i) - miMedia) / miDesv) ^ 4
    Next i
    Curtosis = (n * (n + 1) * suma / ((n - 1) * (n - 2) * (n - 3))) - ((3 * (n - 1) * (n - 1)) / ((n - 2) * (n - 3)))
    Exit Function
etiqueta:
    Curtosis = "No disponible"
End Function

Function Ecuaci�nRecta(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim Pend As Double, Interc As Double 'ojo que no es variant
    'si esto falla es porque no conten�a n�meros, ecuaci�n no disponible
    Pend = PendienteRecta(Vector(), LogEspecial(N�meroElementos(Vector()), False))
    Interc = InterceptoRecta(Vector(), LogEspecial(N�meroElementos(Vector()), False))
    Dim PrimeraParte As String
    Dim SegundaParte As String
    'arma la primera
    Select Case Pend
        Case 0
            'no se muestra la pendiente
            PrimeraParte = ""
        Case 1
            PrimeraParte = "x "
        Case -1
            PrimeraParte = "-x "
        Case Else
            PrimeraParte = Pend & "x "
    End Select
    'arma la segunda
    Select Case Sgn(Interc)
        Case 0
            'no se muestra el intercepto
            SegundaParte = ""
        Case 1
            SegundaParte = IIf(Pend = 0, "", "+ ") & Abs(Interc)
        Case -1
            SegundaParte = "- " & Abs(Interc)
    End Select
    Ecuaci�nRecta = PrimeraParte & SegundaParte
    If Ecuaci�nRecta = "" Then Ecuaci�nRecta = "0"
    Ecuaci�nRecta = "y = " & Ecuaci�nRecta
    Exit Function
etiqueta:
    Ecuaci�nRecta = "No disponible"
End Function

Function PendienteRecta(VectorDependienteY() As Variant, VectorIndependienteX() As Variant) As Variant
On Error GoTo etiqueta
    Dim SumX, SumY, SumXY, SumX2
    Dim n As Long
    Dim i As Long
    n = N�meroElementos(VectorDependienteY())
    If n < 2 Then GoTo etiqueta
    SumX = 0: SumY = 0: SumXY = 0: SumX2 = 0
    For i = LBound(VectorDependienteY()) To UBound(VectorDependienteY())
        SumX = SumX + VectorIndependienteX(i)
        SumY = SumY + VectorDependienteY(i)
        SumXY = SumXY + VectorIndependienteX(i) * VectorDependienteY(i)
        SumX2 = SumX2 + VectorIndependienteX(i) * VectorIndependienteX(i)
    Next i
    PendienteRecta = (n * SumXY - SumX * SumY) / (n * SumX2 - SumX * SumX)
    Exit Function
etiqueta:
    PendienteRecta = "No disponible"
End Function

Function InterceptoRecta(VectorDependienteY() As Variant, VectorIndependienteX() As Variant) As Variant
On Error GoTo etiqueta
    Dim SumX, SumY, SumXY, SumX2
    Dim n As Long
    Dim i As Long
    n = N�meroElementos(VectorDependienteY())
    If n < 2 Then GoTo etiqueta
    SumX = 0: SumY = 0: SumXY = 0: SumX2 = 0
    For i = LBound(VectorIndependienteX()) To UBound(VectorIndependienteX())
        SumX = SumX + VectorIndependienteX(i)
        SumY = SumY + VectorDependienteY(i)
        SumXY = SumXY + VectorIndependienteX(i) * VectorDependienteY(i)
        SumX2 = SumX2 + VectorIndependienteX(i) * VectorIndependienteX(i)
    Next i
    InterceptoRecta = (SumY * SumX2 - SumX * SumXY) / (n * SumX2 - SumX * SumX)
    Exit Function
etiqueta:
    InterceptoRecta = "No disponible"
End Function
'******************************
'par�metro a, modelo exponencial y=b*m^x � y=b*e^ax
Function aModeloExp(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorx = LogEspecial(n, False)
    aModeloExp = PendienteRecta(Vectorlny(), Vectorx())
    Exit Function
etiqueta:
    aModeloExp = "No disponible"
End Function
'par�metro b, modelo exponencial y=b*m^x � y=b*e^ax
Function bModeloExp(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorx = LogEspecial(n, False)
    bModeloExp = InterceptoRecta(Vectorlny(), Vectorx())
    bModeloExp = Exp(bModeloExp)
    Exit Function
etiqueta:
    bModeloExp = "No disponible"
End Function
'par�metro m, modelo exponencial y=b*m^x � y=b*e^ax
Function mModeloExp(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorx = LogEspecial(n, False)
    mModeloExp = Exp(PendienteRecta(Vectorlny(), Vectorx()))
    Exit Function
etiqueta:
    mModeloExp = "No disponible"
End Function
'Ecuaci�n exponencial y=b*m^x � y=b*e^ax como texto
Function Ecuaci�nExp(VectorDependienteY() As Variant, mBase As Boolean) As Variant
On Error GoTo etiqueta
    Dim A As Double, B As Double, m As Double
    'si esto falla por ser double no conten�an n�meros
    A = aModeloExp(VectorDependienteY())
    B = bModeloExp(VectorDependienteY())
    m = mModeloExp(VectorDependienteY())
    If mBase Then
        Ecuaci�nExp = "y = " & B & " * " & m & " ^ x"
    Else
        Ecuaci�nExp = "y = " & B & " * e^(" & A & " * x)"
    End If
    Exit Function
etiqueta:
    Ecuaci�nExp = "No disponible"
End Function
'Coef R cuadrado, modelo exponencial y=b*m^x � y=b*e^ax
Function R2ModeloExp(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorx = LogEspecial(n, False)
    R2ModeloExp = RCuadrado(Vectorlny(), Vectorx())
    Exit Function
etiqueta:
    R2ModeloExp = "No disponible"
End Function
'*******************************************
'par�metro a, modelo Potencial y=a*x^b
Function aModeloPot(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorlnx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorlnx = LogEspecial(n, True)
    aModeloPot = Exp(InterceptoRecta(Vectorlny(), Vectorlnx()))
    Exit Function
etiqueta:
    aModeloPot = "No disponible"
End Function
'par�metro b, modelo Potencial y=a*x^b
Function bModeloPot(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorlnx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorlnx = LogEspecial(n, True)
    bModeloPot = PendienteRecta(Vectorlny(), Vectorlnx())
    Exit Function
etiqueta:
    bModeloPot = "No disponible"
End Function
'Ecuaci�n Potencial y=a*x^b como texto
Function Ecuaci�nPot(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim A As Double, B As Double
    'si esto falla por ser double no conten�an n�meros
    A = aModeloPot(VectorDependienteY())
    B = bModeloPot(VectorDependienteY())
    Ecuaci�nPot = "y = " & A & " * x ^ " & B
    Exit Function
etiqueta:
    Ecuaci�nPot = "No disponible"
End Function

'Coef R cuadrado, modelo Potencial y=a*x^b
Function R2ModeloPot(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlny(), Vectorlnx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlny = LnArray(VectorDependienteY())
    Vectorlnx = LogEspecial(n, True)
    R2ModeloPot = RCuadrado(Vectorlny(), Vectorlnx())
    Exit Function
etiqueta:
    R2ModeloPot = "No disponible"
End Function
'*******************************************
'par�metro a, modelo logar�tmico y=a*ln(x)+b
Function aModeloLog(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlnx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlnx = LogEspecial(n, True)
    aModeloLog = PendienteRecta(VectorDependienteY(), Vectorlnx())
    Exit Function
etiqueta:
    aModeloLog = "No disponible"
End Function
'par�metro b, modelo logar�tmico y=a*ln(x)+b
Function bModeloLog(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlnx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlnx = LogEspecial(n, True)
    bModeloLog = InterceptoRecta(VectorDependienteY(), Vectorlnx())
    Exit Function
etiqueta:
    bModeloLog = "No disponible"
End Function
'Ecuaci�n Logar�tmica y=a*ln(x)+b como texto
Function Ecuaci�nLog(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim A As Double, B As Double
    'si esto falla por ser double no conten�an n�meros
    A = aModeloLog(VectorDependienteY())
    B = bModeloLog(VectorDependienteY())
    Dim Interce As String
    Select Case Sgn(B)
        Case 1
            Interce = " + " & B
        Case 0
            Interce = ""
        Case -1
            Interce = " - " & Abs(B)
    End Select
    Ecuaci�nLog = "y = " & A & " * ln(x)" & Interce
    Exit Function
etiqueta:
    Ecuaci�nLog = "No disponible"
End Function

'Coef R cuadrado, modelo Logar�tmico y=a*ln(x)+b
Function R2ModeloLog(VectorDependienteY() As Variant) As Variant
On Error GoTo etiqueta
    Dim Vectorlnx()
    Dim n As Long
    n = N�meroElementos(VectorDependienteY())
    Vectorlnx = LogEspecial(n, True)
    R2ModeloLog = RCuadrado(VectorDependienteY(), Vectorlnx())
    Exit Function
etiqueta:
    R2ModeloLog = "No disponible"
End Function

'/////////////////////////////////////////////
Function CoeficienteDeterminaci�n(VectorIndependienteY() As Variant, VectorDependienteX() As Variant) As Variant
'R2 sin cuadrado, modelo lineal
On Error GoTo etiqueta
    Dim SumX, SumY, SumXY, SumX2, SumY2
    Dim n As Long
    Dim i As Long
    n = N�meroElementos(VectorIndependienteY())
    If n < 2 Then GoTo etiqueta
    SumX = 0: SumY = 0: SumXY = 0: SumX2 = 0: SumY2 = 0
    For i = LBound(VectorIndependienteY()) To UBound(VectorIndependienteY())
        SumX = SumX + VectorDependienteX(i)
        SumY = SumY + VectorIndependienteY(i)
        SumXY = SumXY + VectorDependienteX(i) * VectorIndependienteY(i)
        SumX2 = SumX2 + VectorDependienteX(i) * VectorDependienteX(i)
        SumY2 = SumY2 + VectorIndependienteY(i) * VectorIndependienteY(i)
    Next i
    CoeficienteDeterminaci�n = (n * SumXY - SumX * SumY) / (Sqr((n * SumX2 - SumX * SumX) * (n * SumY2 - SumY * SumY)))
    Exit Function
etiqueta:
    CoeficienteDeterminaci�n = "No disponible"
End Function

'/////////////////////////////////////////////
Function R2ModeloPol(GradoPol As Integer, VectorIndependienteY() As Variant) As Variant
'R2 sin cuadrado, modelo lineal
On Error GoTo etiqueta
    Dim SSE As Double, SST As Double
    Dim SumY As Double, SumY2 As Double
    Dim n As Long
    Dim i As Long
    Dim MiPolAjuste
    n = N�meroElementos(VectorIndependienteY())
    If n < 2 Then GoTo etiqueta
    SumY = 0: SumY2 = 0
    MiPolAjuste = PolinomioAjuste(GradoPol, VectorIndependienteY(), LogEspecial(n, False))
    For i = LBound(VectorIndependienteY()) To UBound(VectorIndependienteY())
        SumY = SumY + VectorIndependienteY(i)
        SumY2 = SumY2 + VectorIndependienteY(i) * VectorIndependienteY(i)
        SSE = (VectorIndependienteY(i) - EstimarY(i, Polin�mico, MiPolAjuste)) ^ 2
    Next i
    SST = SumY2 - SumY * SumY / n
    R2ModeloPol = Abs(1 - SSE / SST)
    Exit Function
etiqueta:
    R2ModeloPol = "No disponible"
End Function
'Estima el valor Y a partir de x dado, seg�n el modelo
Function EstimarY(x, MiModelo As Modelo, ParamArray Par�metros()) As Variant
    'Enum Modelo est� definido como
    'Lineal = 1
    'Exponecial = 2
    'Potencial = 3
    'Logar�tmico = 4
    'Polin�mico = 5
    'recordar
    'modelo exponencial y=b*m^x � y=b*e^ax
    'modelo Potencial y=a*x^b
    'modelo logar�tmico y=a*ln(x)+b
On Error GoTo etiqueta
    Dim VectorCoeF() As Variant, NumCoef As Integer, Term As Integer
    EstimarY = 0
    Select Case MiModelo
        Case Lineal
            EstimarY = Par�metros(0) + Par�metros(1) * x
        Case Exponecial
            EstimarY = Par�metros(0) * Exp(Par�metros(1) * x)
        Case Potencial
            EstimarY = Par�metros(0) * (x ^ Par�metros(1))
        Case Logar�tmico
            EstimarY = Par�metros(0) * Log(x) + Par�metros(1)
        Case Polin�mico
            VectorCoeF() = Par�metros(0)  'el �nico par�metro es un array
            NumCoef = UBound(VectorCoeF)
            For Term = 1 To NumCoef
                EstimarY = EstimarY + VectorCoeF(Term) * (x ^ (Term - 1))
            Next Term
    End Select
    Exit Function
etiqueta:
    EstimarY = "No disponible"
End Function
Function RCuadrado(VectorIndependienteY() As Variant, VectorDependienteX() As Variant) As Variant
On Error GoTo etiqueta
    RCuadrado = CoeficienteDeterminaci�n(VectorIndependienteY(), VectorDependienteX()) ^ 2
    Exit Function
etiqueta:
    RCuadrado = "No disponible"
End Function

Function Tendencia(Vector() As Variant) As Variant
    
    On Error GoTo etiqueta
        
        Select Case PendienteRecta(Vector(), LogEspecial(N�meroElementos(Vector()), False))
        
        Case "No disponible"
            Tendencia = "No disponible"
        Case Is > 0
            Tendencia = "Creciente"
        Case Is < 0
            Tendencia = "Decreciente"
        Case Is = 0
            Tendencia = "Indefinida"
        Case Else
            Tendencia = "No disponible"
        End Select
        
    Exit Function
etiqueta:
    Tendencia = "No disponible"

End Function

Function PrediceLineal(Vector() As Variant, ByVal NumPeriodos As Double) As Variant
    On Error GoTo etiqueta
        Dim n As Long
        n = N�meroElementos(Vector())
        Select Case RCuadrado(Vector(), LogEspecial(n, False))
            Case "No disponible"
                PrediceLineal = "No disponible"
            Case Is >= 0.8 'valor subjetivo, algunos sugieren 0.9 � 0.95
                PrediceLineal = PendienteRecta(Vector(), LogEspecial(n, False)) * (n + NumPeriodos) + InterceptoRecta(Vector(), LogEspecial(n, False))
            Case Else
                PrediceLineal = "No aplica"
        End Select
    Exit Function
etiqueta:
    PrediceLineal = "No disponible"
End Function

Function Varianza(Vector() As Variant, Optional ByVal Poblacional As Boolean = True) As Variant
    'si poblacional es falso se halla la muestral
    On Error GoTo etiqueta
    Dim Divisor As Long
    If Poblacional Then
        Divisor = N�meroElementos(Vector())
    Else
        Divisor = N�meroElementos(Vector()) - 1
    End If
    'no tocar, f�rmula peligrosa
    Varianza = (SumaCuadrados(Vector()) - (SumaVector(Vector()) * Promedio(Vector()))) / Divisor
    Exit Function
etiqueta:
    Varianza = "No disponible"
End Function

Function Covarianza(Vector1() As Variant, Vector2() As Variant) As Variant
On Error GoTo etiqueta
    Dim n As Long
    Dim i As Long
    Dim temporal As Double
    'no tocar, f�rmula peligrosa
    If (UBound(Vector1()) <> UBound(Vector2())) Or (LBound(Vector1()) <> LBound(Vector2())) Then
        'n�mero de datos no coincide
        Covarianza = "No disponible"
    Else
        n = N�meroElementos(Vector1()) 'es el mismo que el de vector2
        'ojo, dos pares de datos
        If n < 2 Then GoTo etiqueta ' datos insuficientes
        temporal = 0 'almacena la suma del producto
        For i = LBound(Vector1()) To UBound(Vector1())
            temporal = temporal + Vector1(i) * Vector2(i)
        Next i
        Covarianza = (temporal / n) - (Promedio(Vector1()) * Promedio(Vector2()))
    End If
        
    Exit Function
etiqueta:
    Covarianza = "No disponible"
End Function

Function CoeficienteCorrelaci�n(miVector1() As Variant, miVector2() As Variant) As Variant
    On Error GoTo etiqueta
    'cociente entre la covarianza y el producto de las desviaciones t�picas
    Dim Micov As Variant
    Micov = Covarianza(miVector1(), miVector2())
    If Micov = "No disponible" Then GoTo etiqueta
    CoeficienteCorrelaci�n = Micov / (Desviaci�nEst�ndar(miVector1()) * Desviaci�nEst�ndar(miVector2()))
    Exit Function
etiqueta:
    CoeficienteCorrelaci�n = "No disponible"
End Function

Function CoeficienteVariaci�n(Vector() As Variant) As Variant
    On Error GoTo etiqueta
    CoeficienteVariaci�n = Desviaci�nEst�ndar(Vector()) / Promedio(Vector())
    Exit Function
etiqueta:
    CoeficienteVariaci�n = "No disponible"
End Function

Function SumaVector(Vector() As Variant) As Variant
On Error GoTo etiqueta
    Dim i As Long
    Dim suma As Double
    suma = 0
    For i = LBound(Vector()) To UBound(Vector())
        suma = Vector(i) + suma
    Next i
    SumaVector = suma
    Exit Function
etiqueta:
SumaVector = "No disponible"
End Function

Function N�meroElementos(Vector() As Variant) As Variant
    On Error GoTo etiqueta
    N�meroElementos = (UBound(Vector()) - LBound(Vector())) + 1
    Exit Function
etiqueta:
    N�meroElementos = "No disponible"
End Function

Function SumaCuadrados(Vector() As Variant) As Variant
    On Error GoTo etiqueta
    Dim suma As Double
    Dim i As Long
    suma = 0
    For i = LBound(Vector()) To UBound(Vector())
        suma = Vector(i) * Vector(i) + suma
    Next i
    SumaCuadrados = suma
    Exit Function
etiqueta:
    SumaCuadrados = "No disponible"
End Function

' polymorphic sort routine that works with any type of array

Sub ShellSortAny(arr As Variant, numEls As Long, descending As Boolean)
    Dim Index As Long, index2 As Long
    Dim firstItem As Long, inverseOrder As Boolean
    Dim distance As Long, value As Variant
    ' exit if it is not an array
    If VarType(arr) < vbArray Then Exit Sub
    firstItem = LBound(arr)
    ' find the best value for distance
    Do
        distance = distance * 3 + 1
    Loop Until distance > numEls
    ' sort the array
    Do
        distance = distance \ 3
        For Index = distance + 1 To numEls
            value = arr(Index)
            index2 = Index
            Do While (arr(index2 - distance) > value) Xor descending
                arr(index2) = arr(index2 - distance)
                index2 = index2 - distance
                If index2 <= distance Then Exit Do
            Loop
            arr(index2) = value
        Next
    Loop Until distance = 1
End Sub

'Devuelve un vector con los logaritmos naturales del vector argumento
'Si alg�n elemento es no positivo devuelve error 5
Function LnArray(Vector() As Variant) As Variant()
On Error GoTo etiqueta
    Dim newArray()
    Dim i As Long
    ReDim newArray(LBound(Vector()) To UBound(Vector()))
    For i = LBound(Vector()) To UBound(Vector())
        newArray(i) = Log(Vector(i))
    Next i
    LnArray = newArray()
    Exit Function
etiqueta:
    Err.Clear
    Err.Raise 5
End Function

'Devuelve el vector especial (1,2,3,4...n) �til en estad�stica.
'Si el segundo argumento es verdadero devuelve
'los logaritmos naturales del vector especial (1,2,3,4...n)
Function LogEspecial(n As Long, Optional ReturnLog As Boolean = True) As Variant()
On Error GoTo etiqueta
    Dim i As Long
    If n < 1 Then GoTo etiqueta
    Dim newArray()
    ReDim newArray(1 To n)
    If ReturnLog Then
        For i = 1 To n
            newArray(i) = Log(i)
        Next i
    Else
        For i = 1 To n
            newArray(i) = i
        Next i
    End If
    LogEspecial = newArray()
    Exit Function
etiqueta:
Err.Clear
Err.Raise 5
End Function

'Devuelve true si el vector argumento solo contiene valores
'mayores que cero
Function SoloPositivos(Vector() As Variant) As Boolean
On Error GoTo etiqueta
    Dim i As Long
    For i = LBound(Vector()) To UBound(Vector())
        If Vector(i) <= 0 Then Exit Function
    Next i
    SoloPositivos = True
    Exit Function
etiqueta:
    Err.Clear
    Err.Raise 5
End Function
