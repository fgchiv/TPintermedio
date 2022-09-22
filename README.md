# TPintermedio

La que le da un poco de sentido al proyecto más allá de resolver el TP es ser algo así como un sitio que permita publicar ideas y valorar acuerdo / desacuerdo con una escala Likert. Esto explica los atributos de las clases de "models.py".
Por lo demás:
  - /crearEditor/ es la página para crear un nuevo Editor
  - /crearLector/ es la página que permite crear un nuevo Lector
  . /pensarIdea/ es la página que permite crear un nuevo objeto clase idea (en honor a Twitter tienen un límite de extensión de 280 caracteres)
  - /buscarenIdea/ realiza una búsqueda en el texto de las ideas y devuelve las ideas.texto e ideas.tema
  
Me hubiera gustado mandarlo un poco más completo (y con la base de datos un poco más llena), pero no lo quiero dedicar más tiempo a un trabajo intermedio.
Las cosas agregadas que quería hacer son:
  - que la búsqueda fuera en Ideas.texto e Ideas.tema
  - armar la lógica y las páginas para que las valoraciones dadas a cada idea se almacenen y poder mostrarlas
  - asociar los objetos de la clase editor a sus ideas
    
