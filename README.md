# Bitácora de Gimnasio

Una app personal para registrar el gimnasio. Corre como artefacto en claude.ai.

Tiene cuatro pestañas:

- **Rutina:** registrar series, peso y repeticiones.
- **Progreso:** gráficas.
- **Salud:** peso, medidas con cinta, báscula de bioimpedancia, IMC y grasa estimada.
- **Configuración:** biblioteca de ejercicios, unidad kg/lb y respaldo.

Es de **uso individual**: cada persona publica su propia copia y solo ella la ve.

La copia original está en https://claude.ai/artifact/1CFgAFbsMrYmP6BFnihpZ4.

## Qué hay aquí

| Archivo | Contenido |
|---|---|
| `index.html` | La app completa en un solo archivo: HTML, CSS, JavaScript y la biblioteca de ejercicios incrustada. |
| `capabilities.json` | Capacidades del artefacto: `db`, `user`, `assets` y `downloads`. Solo la dueña o el dueño puede leer y escribir. |
| `assets/` | Las 224 imágenes de ejercicios y músculos. |
| `data/exercises/*.json` | La biblioteca de ejercicios (109), un archivo por ejercicio. Las imágenes aparecen como `/_blob/<id>`, que es el mismo `<id>` del archivo en `assets/`. |
| `data/media/musculos.json` | La imagen y el crédito de cada grupo muscular. |
| `tools/embed_seed.py` | Copia `data/` dentro de `index.html` (ver abajo). |
| `extras/rutinas-camila.json` | Tres rutinas listas para importar: Cuádriceps y Glúteos, Espalda y Bíceps, Femorales y Glúteos. |

Las imágenes de ejercicios vienen de *free-exercise-db*, que es de dominio público. Las de músculos vienen de Wikimedia Commons y BodyParts3D; la licencia de cada una está en `musculos.json`.

**Datos personales:** este repositorio no tiene rutinas, sesiones, medidas ni ajustes de nadie. La única excepción es el archivo de `extras/`. Los datos personales viven en la base de datos privada de cada artefacto.

## Tener tu propia copia

Necesitas la app de Claude con la pestaña **Code** (Claude Code).

1. Descarga este repositorio. Puedes usar **Code → Download ZIP** en GitHub y descomprimirlo, o `git clone`.
2. En Claude Code, abre esa carpeta y pídele:

   > Publica `index.html` como un artefacto nuevo. Usa las capacidades de `capabilities.json` y sube todos los archivos de la carpeta `assets/` como archivos del artefacto, en la misma ruta `assets/<nombre>`.

3. Abre el enlace del artefacto. La primera vez la app carga sola los 109 ejercicios de la biblioteca: verás el aviso "Cargando la biblioteca de ejercicios…".
4. Si quieres las rutinas de `extras/`, ve a **Configuración → Respaldo → Importar** y elige `extras/rutinas-camila.json`. Eso solo agrega rutinas, no borra nada.

La copia es tuya. Nadie más la ve a menos que la compartas desde el menú **Compartir**.

## Abrirlo fuera de claude.ai

Si abres `index.html` directamente en el navegador, desde la carpeta del repositorio, la app funciona en modo local: guarda todo en el `localStorage` de ese navegador. También carga la biblioteca con sus imágenes de `assets/`.

## Respaldar tus datos

Usa **Configuración → Exportar** dentro de la app. Eso descarga un JSON con tus rutinas, sesiones, medidas y notas. Para recuperarlo, usa **Importar**.

## Actualizar este repositorio

- **Si cambia la app:** guarda el HTML en `index.html`, haz commit y luego push.
- **Si cambia la biblioteca:**
  1. Exporta de nuevo la colección `exercises` a `data/exercises/`.
  2. Pon las imágenes nuevas en `assets/<id>.<ext>`.
  3. Corre `python3 tools/embed_seed.py`, que actualiza el bloque `SEED_LIB` de `index.html`.
  4. Haz commit.

La biblioteca incrustada solo se usa cuando la base de datos de una copia está vacía, así que no toca una copia que ya tiene ejercicios.
