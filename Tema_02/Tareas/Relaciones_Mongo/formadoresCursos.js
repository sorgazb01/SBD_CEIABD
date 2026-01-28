use('modelo_empresa')

db.cursos.aggregate([
  { $unwind: "$formadores" },
  { $lookup: { from: "personas", localField: "formadores.personaId", foreignField: "_id", as: "formador" } },
  { $unwind: "$formador" },
  {
    $group: {
      _id: "$_id",
      titulo: { $first: "$titulo" },
      categoria: { $first: "$categoria" },
      horas: { $first: "$horas" },
      modalidad: { $first: "$modalidad" },
      formadores: { $push: { _id: "$formador._id", nombre: "$formador.nombre", apellidos: "$formador.apellidos", puesto: "$formador.puesto" } }
    }
  }
])