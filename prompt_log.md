# Prompt Log

## Prompt 1 - Instruction de Github Copilot

Archivo de instrucciones en `.github/instructions/copilot-instructions.instruction.md`. Es la dinámica con la que estoy generando proyectos con Copilot y me está funcionando perfectamente. Gracias a este archivo, soy capaz de proporcionar todo el contexto del proyecto, arquitectura y reglas de desarrollo. 

Además, le sirve a Copilot como hoja de ruta en la que se va guardando el progreso y las tareas realizadas. De este modo, evito uno de los problemas que generalmente ocurren al trabajar con IA en proyectos grandes durante mucho tiempo: la pérdida de contexto y la falta de cohesión. 

El motivo por el que está en inglés es simple: las IAs están entrenadas en inglés, y tanto la documentación técnica como los ejemplos de código también lo están. Por lo tanto, los prompts en inglés generan mejores outputs y son más consistentes.

## Prompt 2 - Fases y Tareas

Dada la estructura y claridad del prompt 1, la realización del proyecto es tan sencilla como ir pidiéndole a Copilot, fase por fase, las diferentes tareas ('Generate task 3 of phase 2.'). Cuando te genera el código de cada tarea, se revisa, se cambian partes específicas o pequeños debugs y se continúa con la siguiente. Cuanto más concreta y profesional sea la instruction, más fiel a lo que se desea conseguir será lo proporcionado por Copilot, lo que se traduce en menos bugs o código innecesario / inventado.

## Prompt 3 - Ejemplo de instruction incompleta

Al empezar a trabajar con la fase 2, revisando lo propuesto por Copilot me doy cuenta de que está generando lógica, endpoints y configuración en el main. Obviamente, la culpa no es de Copilot, si no de que no estaba especificado inicialmente en la instruction. Tras cambiarla para clarificar que se trabaje bajo el principio de responsabilidad única e indicar la estructura de directorios del proyecto deseada y qué debe ir en cada directorio, se le pide a Copilot que revise los cambios en la instruction y adapte su respuesta anterior a los mismos.

## Prompt 4 - Sobreescritura de estilos de BootStrap

Siendo honesto, tengo experiencia trabajando en Frontend y no me supone un problema, pero diseñar el estilo o elegir paleta de colores no es algo que se me dé del todo bien. Por ello, genero `frontend\src\assets\main.css`, y le pido a Copilot que me proporcione ejemplos de css para sobreescribir algunos de los estilos predeterminados que ofrece BootStrap y así ofrecer una experiencia de usuario distinta a la que viene por defecto.
