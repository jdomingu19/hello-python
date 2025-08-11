Attribute VB_Name = "VARIOS"
Option Explicit

Sub Main()
    'salir si se ha ejecutado otra instancia, cuando se compile
    If App.PrevInstance Then
        End
    End If
    'bienvenida
    frmSplash.Show
    frmSplash.Refresh
    frmMatrices.Show
    'no hay eventos hasta que se quite la bienvenida
    frmMatrices.Enabled = False
    'se asegura de que esté encima
    frmSplash.SetFocus
End Sub

'***********************
' Preparar la anchura del control flexgrid de tal forma que cada elemento sea
' plenamente visible, si el segundo argumento es True, la anchura de los
' títulos de las columnas también se tiene en cuenta.

Sub FlexGridAdjustColumnWidth(Flex As MSHFlexGrid, Optional AccountForHeaders _
    As Boolean)
    On Error Resume Next
    Dim row As Long, Col As Long
    Dim width As Single, maxWidth As Single
    Dim saveFont As StdFont, saveScaleMode As Integer
    Dim cellText As String
    ' salir si no hay elementos
    If Flex.Rows = 0 Then Exit Sub
    
    ' guardar la fuente utilizada por el formulario padre y forzar la fuente
    ' Flexgrid. Necesitamos hacer esta operación para utilizar el método
    ' TextWidth del formulario.
    Set saveFont = Flex.Parent.Font
    Set Flex.Parent.Font = Flex.Font
    ' forzar ScaleMode = vbTwips para el padre
    saveScaleMode = Flex.Parent.ScaleMode
    Flex.Parent.ScaleMode = vbTwips
    
    For Col = 0 To Flex.cols - 1
        maxWidth = 0
        If AccountForHeaders Then
            maxWidth = Flex.Parent.TextWidth(Flex.TextMatrix(0, Col)) + 205
        End If
        For row = 1 To Flex.Rows - 1
            ' recuperar la cadena de texto
            cellText = Flex.TextMatrix(row, Col)
            ' calcular su anchura, teniendo en cuenta los márgenes
            ' nota: no tener en cuenta campos de texto de varias líneas
            width = Flex.Parent.TextWidth(cellText) + 205
            ' actualizar maxWidth si se localiza una cadena de mayor longitud
            If width > maxWidth Then maxWidth = width
        Next
        ' modificar la anchura de la columna
        Flex.ColWidth(Col) = maxWidth
    Next
    
    ' restaurar las propiedades del formulario padre
    Set Flex.Parent.Font = saveFont
    Flex.Parent.ScaleMode = saveScaleMode
End Sub
'******************************************************
' $DESCR True si una variable contiene un valor numérico válido.
' $DESCR Puede rechazar valores no enteros, puede rechazar números en notación científica
' $DESCR Rechaza cadenas vacías y acepta límites
Function CheckNumeric(Text As Variant, Optional DecValue As Boolean = False, Optional Min As Variant, Optional Max As Variant, Optional Scientific As Boolean = False) As Boolean
    Dim i As Integer, decSep As String, Temp As Double
    On Error GoTo Salir
    'rechazar cualquier cosa vacía, nula o no inicializada
    If IsNull(Text) Then Exit Function
    If IsEmpty(Text) Then Exit Function
    If Len(Text) = 0 Then Exit Function
    'esta asignación valida varias cosas, entre ellas la notación científica
    'asignación de prueba
    Temp = Text
    ' recupera el separador decimal
    decSep = Format$(0.1, ".")
    For i = 1 To Len(Text)
        Select Case Mid$(Text, i, 1)
            Case "0" To "9"
                'los números son válidos
            Case "-", "+"
                'cuando se admite notación científica
                'pueden existir 2 signos +/-, el del valor y el del exponente
                'por ejemplo: -2.23E-15
                If Scientific Then
                'cuando no se admite notación científica
                Else
                    ' el signo más/menos solo se permite
                    ' como caracter inicial
                    If i > 1 Then Exit Function
                End If
            Case decSep
                ' salir si no se permiten valores decimales
                If Not DecValue Then Exit Function
                ' solo se permite un separador decimal
                If InStr(1, Text, decSep, vbTextCompare) < i Then Exit Function
                ' el separador decimal no puede estar solo
                If Len(Text) = 1 Then Exit Function
            Case "e", "E"
                ' salir si no se permite notación científica
                If Not Scientific Then Exit Function
                'en realidad no se requiere validar
                'ya que la asignación de prueba efectúa el trabajo
                ' solo se permite una E
                If InStr(1, Text, "E", vbTextCompare) < i Then Exit Function
                ' la E no puede estar sola
                If Len(Text) = 1 Then Exit Function
            Case Else
                ' rechazar cualquier otro caracter
                Exit Function
        End Select
    Next
    'validar límites si se pasaron los argumentos Min y Max
    If Not IsMissing(Min) Then
        If CDbl(Text) < CDbl(Min) Then Exit Function
    End If
    If Not IsMissing(Max) Then
        If CDbl(Text) > CDbl(Max) Then Exit Function
    End If
    CheckNumeric = True 'es un valor numérico válido
Salir:
End Function
Function InterpretarDecimal(ByRef KeyAscii As Integer)
    'interpreta tanto el punto(.) como la coma(,)
    'como separadores decimales
    Dim SepDec As String
    SepDec = Format$(0.1, ".")
    If Len(SepDec) = 1 And (KeyAscii = 46 Or KeyAscii = 44) Then 'si presiona punto o coma
        KeyAscii = Asc(SepDec) 'transforma keyascii en el separador correcto
    End If
End Function

'copia un flexgrid en otro
Function CopyFlex(FlexOrigen As MSHFlexGrid, FlexDestino As MSHFlexGrid) As Boolean
    On Error GoTo etiqueta
    Dim i As Integer
    Dim J As Integer
    'valida igualdad de tamaños
    If FlexOrigen.Rows <> FlexDestino.Rows Or FlexOrigen.cols <> FlexDestino.cols Then GoTo etiqueta
    For i = 1 To FlexOrigen.Rows - 1
        For J = 1 To FlexOrigen.cols - 1
            If CheckNumeric(FlexOrigen.TextMatrix(i, J), True, , , True) Then
                FlexDestino.TextMatrix(i, J) = FlexOrigen.TextMatrix(i, J)
            Else
                Dim msg As String
                Dim Separador As String
                Separador = Format$(0.1, ".")
                msg = "La expresión en la fila " & i & ", columna " & J & " no es un valor numérico válido." & vbCrLf
                msg = msg & vbCrLf & "Ejemplos de expresiones admitidas:"
                msg = msg & vbCrLf & "235" & Separador & "39"
                msg = msg & vbCrLf & "-48" & Separador & "254254"
                msg = msg & vbCrLf & "1E+6"
                msg = msg & vbCrLf & "-2" & Separador & "37E-17"
                msg = msg & vbCrLf & "¡No se admite el separador de millar!"
                msg = msg & vbCrLf & vbCrLf & "Recuerde que su separador decimal es: " & Separador
                MsgBox msg, vbCritical, "Error en la matriz " & FlexOrigen.Name
                'lo activo para que setfocus no falle
                frmMatrices.Enabled = True
                If FlexOrigen.Enabled And FlexOrigen.Visible Then FlexOrigen.SetFocus
                FlexOrigen.Col = J
                FlexOrigen.row = i
                frmMatrices.CallSelChangeByName FlexOrigen.Name
                Exit Function
            End If
        Next J
    Next i
    CopyFlex = True
    Exit Function
etiqueta:
Err.Clear
End Function
'convierte una cadena delimitada en una matriz
Public Function Cadena_MatrizDelimitada(Cadena As String) As Variant
    'advertencia: se usa la función SplitMulti porque la función
    'Split intrínsica de VB no trabaja con delimitadores múltiples como el vbcrlf
    Dim i, J
    Dim VectorFilas, VectorColumnas, V
    'elimina los caracteres innecesarios al final del archivo
    Do While Len(Cadena) > 0
        Debug.Print "¿vbcr? = " & (Right$(Cadena, 1) = vbCr)
        Debug.Print "¿vblf? = " & (Right$(Cadena, 1) = vbLf)
        Debug.Print "¿vbtab? = " & (Right$(Cadena, 1) = vbTab)
        Select Case Right$(Cadena, 1)
            Case vbCr, vbLf, vbTab
                Cadena = Left$(Cadena, Len(Cadena) - 1)
            Case Else
                Exit Do
        End Select
    Loop
    'obtiene las filas, están separadas por retorno de carro
    VectorFilas = SplitMulti(Cadena, vbCrLf)
    For i = 0 To UBound(VectorFilas, 1)
        'obtiene las columnas, separadas por tabulador
        VectorColumnas = Split(VectorFilas(i), vbTab)
        'prepara el vector, supone que todas las filas contienen igual número de valores
        If i = 0 Then
            'solo la primera vez
            ReDim V(1 To UBound(VectorFilas, 1) + 1, 1 To UBound(VectorColumnas, 1) + 1)
        End If
        For J = 0 To UBound(VectorColumnas, 1)
            V(i + 1, J + 1) = VectorColumnas(J)
            'Debug.Print "[" & i & ", " & J & "] = " & V(i, J) & "  ;"
        Next
    Next
    Cadena_MatrizDelimitada = V
End Function
'lee una matriz de un archivo de matrices
Public Sub ArchivoArray(V As Variant, filename As String)
    'lee el archivo
    Dim Contenido As String
    Contenido = ReadTextFileContents(filename)
    V = Cadena_MatrizDelimitada(Contenido)
End Sub
'convierte una matriz en una cadena delimitada
Function MatrizDelimitada_Cadena(V As Variant) As String
    Dim Contenido As String
    Dim i, J
    Dim numFilas As Integer
    Dim numCols As Integer
    numFilas = UBound(V, 1)
    numCols = UBound(V, 2)
    Contenido = ""
    For i = 1 To numFilas
        For J = 1 To numCols
            'agrega el valor del vector
            Contenido = Contenido & V(i, J)
            'agrega una tabulación para separar columnas
            Contenido = Contenido & vbTab
        Next
        'elimina el tab de la última columna
        Contenido = Left$(Contenido, Len(Contenido) - 1)
        'retorno de carro y avance de línea para separar filas
        Contenido = Contenido & vbCrLf
    Next
    'elimina los caracteres innecesarios al final de la cadena
    Do While Len(Contenido) > 0
        Debug.Print "vbcr" & (Right$(Contenido, 1) = vbCr)
        Debug.Print "vblf" & (Right$(Contenido, 1) = vbLf)
        Debug.Print "vbtab" & (Right$(Contenido, 1) = vbTab)
        Select Case Right$(Contenido, 1)
            Case vbCr, vbLf, vbTab
                Contenido = Left$(Contenido, Len(Contenido) - 1)
            Case Else
                Exit Do
        End Select
    Loop
    MatrizDelimitada_Cadena = Contenido
End Function
'escribe la matriz en un archivo de matrices
Public Sub ArrayArchivo(V As Variant, filename As String)
    Dim m As New CRaton
    m.DefPuntero vbHourglass
    Dim bloq As New CBloqueo
    bloq.DefEstado frmMatrices, False
    Dim MiCadena As String
    MiCadena = MatrizDelimitada_Cadena(V)
    'almacena la cadena en el archivo indicado
    WriteTextFileContents MiCadena, filename, False
End Sub
' returns the entire contents of a text file as a string
Function ReadTextFileContents(filename As String) As String
    Dim fnum As Integer, isOpen As Boolean
    On Error GoTo Error_Handler
    ' get the next free file number
    fnum = FreeFile()
    Open filename For Input As #fnum
    ' if execution flow got here, the file has been open without error
    isOpen = True
    ' read the entire contents in one single operation
    ReadTextFileContents = Input(LOF(fnum), fnum)
    ' intentionally flow into the error handler to close the file
Error_Handler:
    ' raise the error (if any), but first close the file
    If isOpen Then Close #fnum
    If Err Then Err.Raise Err.number, , Err.Description
End Function

' writes the contents of a string to a file, optionally in Append mode
Sub WriteTextFileContents(Text As String, filename As String, _
    Optional AppendMode As Boolean)
        Dim fnum As Integer, isOpen As Boolean
        On Error GoTo Error_Handler
        ' get the next free file number
        fnum = FreeFile()
        If AppendMode Then
            Open filename For Append As #fnum
        Else
            Open filename For Output As #fnum
        End If
        ' if execution flow got here, the file has been open correctly
        isOpen = True
        ' print to the file in one single operation
        Print #fnum, Text
        ' intentionally flow into the error handler to close the file
Error_Handler:
        ' raise the error (if any), but first close the file
        If isOpen Then Close #fnum
        If Err Then Err.Raise Err.number, , Err.Description
End Sub

' $DESCR A replacement for the built-in Split function, that works with multiple delimited chars.

Function SplitMulti(source As String, delimTable As String, Optional Limit As Long = -1, Optional Compare As VbCompareMethod = vbBinaryCompare) As String()
    Dim i As Long, start As Long, count As Long
    Dim result() As String
    ' we allocate the result array in chunks, to reduce overhead
    Const ALLOC_CHUNK = 50
    ReDim result(0 To ALLOC_CHUNK - 1) As String
    ' parse the string
    For i = 1 To Len(source)
        If InStr(1, delimTable, Mid$(source, i, 1), Compare) Then
            ' we have found a delimiter
            If start Then
                ' if we were in the middle of a word
                If count > UBound(result) Then
                    ' make room in the result array if necessary
                    ReDim Preserve result(0 To UBound(result) _
                        + ALLOC_CHUNK) As String
                End If
                result(count) = Mid$(source, start, i - start)
                start = 0
                count = count + 1
                If count = Limit Then Exit For
            End If
        ElseIf start = 0 Then
            ' this isn't a delimiter - remember where the word starts
            start = i
        End If
    Next
    ' if we were in the middle of a word
    If start And count <> Limit Then
        ' make room in the result array if necessary, or trim it
        ReDim Preserve result(0 To count) As String
        result(count) = Mid$(source, start)
    Else
       ' trim the array to the actual number of items
       ReDim Preserve result(0 To count - 1) As String
    End If
    SplitMulti = result()
End Function


' $DESCR Parse a filename into its components.

Sub SplitFilename(ByVal CompleteName As String, path As String, File As String, Optional Extension As Variant)
    Dim i As Integer
    ' assume there isn't any embedded path
    path = ""
    File = CompleteName
    ' backward search for a path delimiter
    For i = Len(File) To 1 Step -1
        If Mid$(File, i, 1) = "." And Not IsMissing(Extension) Then
            ' we have found an extension and the caller asked for it
            Extension = Mid$(File, i + 1)
            File = Left$(File, i - 1)
        ElseIf InStr(":\", Mid$(File, i, 1)) Then
            ' paths don't have a trailing backslash
            path = Left$(File, i)
            If Right$(path, 1) = "\" Then path = Left$(path, i - 1)
            File = Mid$(File, i + 1)
            Exit For
        End If
    Next
End Sub

' $DESCR The Extension portion of a complete filename.
' $DEPENDENCIES: SplitFilename

Function GetExtension(ByVal CompleteFileName As String) As String
    SplitFilename CompleteFileName, "", "", GetExtension
End Function

' returns the nearest integer equal or higher than the argument
Function Ceiling(number As Double) As Long
    Ceiling = -Int(-number)
End Function
