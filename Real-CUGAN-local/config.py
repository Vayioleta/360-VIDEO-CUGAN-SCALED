##########################################
#################Configuración General#################
##########################################
# Escala de superresolución
scale=2

# Ruta de los modelos, se pueden cambiar
# Versión de reducción de ruido (denoise): recomendada si el original tiene mucho ruido y baja calidad; actualmente, el modelo 2x admite 3 niveles de reducción de ruido;
# Versión sin reducción de ruido (no-denoise): recomendada si el original tiene poco ruido y calidad aceptable, pero se desea mejorar la resolución/nitidez/hacer mejoras generales y reparaciones;
# Versión conservadora (conservative): recomendada si te preocupa perder texturas, el estilo de dibujo cambie, o los colores se intensifiquen, en resumen, si te preocupa que la IA deje marcas de procesamiento notables, se recomienda usar esta versión.
model_path2 = "weights_v3/up2x-latest-denoise3x.pth"
model_path3 = "weights_v3/up3x-latest-denoise3x.pth"
model_path4 = "weights_v3/up4x-latest-denoise3x.pth"

# half: activar la mitad de precisión en tarjetas gráficas antiguas no acelerará el proceso, pero sí ahorrará memoria de la tarjeta; para tarjetas >= serie 20 de NVIDIA, simplemente usa True.
half=True

# Tile más grande ahorra memoria de la tarjeta pero es más lento
tile=5

# cache_mode: si la memoria de la tarjeta está al límite, se puede intentar con 0 o 1 (ambos son sin pérdida); 1 es un 15% más lento pero más eficiente en memoria; si claramente no se puede manejar (por ejemplo, solo 2 GB de memoria para superar >= 720P o imágenes de resoluciones muy grandes como 4K), usa 2 o 3; 2 es un 25% más lento pero con un error adicional del 5% solo en imágenes con desenfoque de profundidad de campo; 3 es un 150% más lento pero sin pérdida.
cache_mode=1

# alpha controla el nivel de reparación de la IA y el tamaño de las marcas; valores más grandes dan menos reparación y marcas más pequeñas, más difuso; valores más pequeños aumentan la reparación, nitidez y cambios en el color (aumento de contraste y saturación); 
# rango ajustable: (0.75,1.3), el valor predeterminado es 1 sin ajuste.
alpha=1

# Modo de superresolución, video o carpeta de imágenes
mode="image"#video#image

############################################
#################  Configuración de Superresolución de Imágenes#################
############################################

# 0 para GPU, si se tienen múltiples GPUs, se pueden escribir 
# configuraciones diferentes y ejecutarlas en paralelo; si se desea usar CPU, rellena "" con cpu.

device="cuda:0"
input_dir="input_dir1" # ruta de imágenes de entrada
output_dir="output_dir" # ruta de salida para imágenes de superresolución

#################Configuración de Superresolución de Videos#################
inp_path=r"input.mp4"
opt_path=r"output.mp4"

# Número de hilos: ajusta según sea necesario, valores bajos reducen la eficiencia, valores altos pueden agotar la memoria de la tarjeta.
nt=2
# Número de tarjetas gráficas
n_gpu=1

# No tocar
p_sleep=(0.005,0.012)
decode_sleep=0.002

# Parámetros de codificación, no tocar si no se entiende; en términos simples, un crf más bajo = alta calidad y alta tasa de bits, slower = baja velocidad de codificación pero alta calidad + mayor uso de CPU, si la CPU no es suficiente, se debería disminuir el nivel, por ejemplo, slow, medium, fast, faster.
encode_params=['-crf', '21', '-preset', 'medium']
