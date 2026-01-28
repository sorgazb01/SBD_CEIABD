use('modelo_empresa')

const IdArea = 1

db.areas.aggregate([
  { $match: { _id: IdArea } },
  { $lookup: { from: "personas", localField: "_id", foreignField: "areaId", as: "personas" } }
])