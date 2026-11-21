# Bitácora de Gimnasio

Respaldo de la app de rutinas de gimnasio que vive como artefacto en claude.ai:
https://claude.ai/artifact/1CFgAFbsMrYmP6BFnihpZ4

La app tiene cinco pestañas:

- **Rutina:** registrar series, peso y repeticiones.
- **Progreso:** gráficas.
- **Salud:** peso, medidas con cinta, báscula de bioimpedancia, IMC y grasa estimada.
- **Juntos:** un calendario compartido entre personas.
- **Configuración:** biblioteca de ejercicios, personas, unidad kg/lb y respaldo.

## Qué hay aquí

| Archivo | Contenido |
|---|---|
| `index.html` | La app completa: HTML, CSS y JavaScript en un solo archivo. Es exactamente lo que está publicado. |
| `capabilities.json` | Capacidades del artefacto (`db`, `user`, `assets`, `downloads`) y las reglas de acceso de la base de datos. |
| `data/exercises/*.json` | La biblioteca compartida de ejercicios (105), un archivo por ejercicio. |
| `data/media/musculos.json` | Imagen y crédito de cada grupo muscular. |
| `assets/<id>.<ext>` | Las 220 imágenes de ejercicios y músculos. El nombre de cada archivo es el id que aparece en los JSON como `/_blob/<id>`. |

Las imágenes de ejercicios vienen de *free-exercise-db* (dominio público). Las de músculos vienen de Wikimedia Commons y BodyParts3D; cada una lleva su licencia en `musculos.json`.

## Qué NO hay aquí

Tus datos personales y los de cada persona no están en este repositorio: rutinas, sesiones, medidas, ajustes, notas y el calendario Juntos. Viven solo en la base de datos privada del artefacto.

Para guardar una copia de esos datos, usa **Configuración → Exportar** dentro de la app. Eso descarga un JSON que después puedes importar.

## Abrirlo fuera de claude.ai

Si abres `index.html` directamente en el navegador, la app funciona en modo local: guarda todo en el `localStorage` de ese navegador. No tendrás la base de datos compartida, la gestión de personas ni las imágenes, porque esas rutas `/_blob/` solo existen dentro del artefacto.

## Cómo restaurar el artefacto si se pierde

1. Publicar `index.html` como artefacto nuevo con las capacidades de `capabilities.json`. Claude Code lo hace con la herramienta Artifact.
2. Subir las imágenes de `assets/` al almacén de assets del artefacto nuevo. Cada imagen recibe un id nuevo, así que hay que reemplazar los `/_blob/<id-viejo>` por los nuevos en los JSON de `data/`.
3. Cargar `data/exercises/*.json` en la colección `exercises` y `data/media/musculos.json` como el documento `media/musculos`.
4. Importar tus datos personales desde el JSON exportado de la app.

## Actualizar este respaldo

Cada vez que cambie la app publicada, hay que copiar el HTML nuevo a `index.html`, hacer commit y hacer push. Si cambió la biblioteca, también hay que volver a exportar `data/`.
