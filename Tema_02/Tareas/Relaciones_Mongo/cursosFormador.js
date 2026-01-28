use('modelo_empresa')

const idFormador = 1

db.personas.aggregate([
  { $match: { _id: idFormador } },
  { $lookup: { from: "cursos", localField: "_id", foreignField: "formadores.personaId", as: "cursos" } },
  { $project: { _id: 1, nombre: 1, apellidos: 1, cursos: 1 } }
])