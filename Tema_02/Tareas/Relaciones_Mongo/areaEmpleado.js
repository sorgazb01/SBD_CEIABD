use('modelo_empresa')

const idEmpleado = 1

db.personas.aggregate([
  { $match: { _id: idEmpleado } }, 
  { $lookup: { from: "areas", localField: "areaId", foreignField: "_id", as: "area" } },
  { $unwind: "$area" },
  { $project: { _id: 1, nombre: 1, apellidos: 1, puesto: 1, "area._id": 1, "area.nombre": 1, "area.ubicacion": 1 } }
])