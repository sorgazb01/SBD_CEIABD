use('modelo_empresa')
db.dropDatabase()

db.areas.insertMany([
    {
        _id: 1,
        nombre: 'Ciberseguridad',
        ubicacion: { ciudad: 'Huelva', direccion: 'C/Jose Manuel Carrion'},
        funciones: ['Gestion de accesos', 'Auditoria', 'Respuestas a incidentes'],
        stack: ['SSO', 'MFA', 'EDR'],
        herramientas: ['Jira', 'Vault']
    },
    {
        _id: 2,
        nombre: 'DevOps',
        ubicacion: { ciudad: 'Cordoba', direccion: 'C/Las Acacias'},
        funciones: ['Docker', 'Kubernetes', 'Redes internas'],
        stack: ['Docker', 'Grafana', 'Terraform'],
        herramientas: ['Velero', 'ELK']
    },
    {
        _id: 3,
        nombre: 'Data',
        ubicacion: { ciudad: 'Talavera de la Reina', direccion: 'C/Cervantes' },
        funciones: ['ETL', 'Bi', 'Gobierno del dato'],
        stack: ['SQL', 'Spark', 'Python'],
        herramientas: ['Power BI', 'BigQuery']
    },
    {
        _id: 4,
        nombre: 'Desarrollo',
        ubicacion: { ciudad: 'Merida', direccion: 'C/Santa Catalina' },
        funciones: ['Backend', 'Frontend', 'QA'],
        stack: ['TypeScript', 'Java', 'PostgreSQL'],
        herramientas: ['GitHub', 'Jira']
    }
])

db.personas.insertMany([
  {
    _id: 1,
    nombre: "Lucía",
    apellidos: "Romero Díaz",
    telefono: "+34 600 111 101",
    puesto: "Analista SOC",
    areaId: 1,
    roles: ["empleado", "formador"],
    modalidadTrabajo: "Híbrido"
  },
  {
    _id: 2,
    nombre: "Iván",
    apellidos: "Serrano López",
    telefono: "+34 600 111 102",
    puesto: "IAM Engineer",
    areaId: 1,
    roles: ["empleado"],
    modalidadTrabajo: "Remoto"
  },
  {
    _id: 3,
    nombre: "Paula",
    apellidos: "Molina Ruiz",
    telefono: "+34 600 222 201",
    puesto: "DevOps Engineer",
    areaId: 2,
    roles: ["empleado", "formador"],
    modalidadTrabajo: "Híbrido"
  },
  {
    _id: 4,
    nombre: "Diego",
    apellidos: "Vega Torres",
    telefono: "+34 600 222 202",
    puesto: "SRE",
    areaId: 2,
    roles: ["empleado"],
    modalidadTrabajo: "Presencial"
  },
  {
    _id: 5,
    nombre: "Nerea",
    apellidos: "Castro Pérez",
    telefono: "+34 600 333 301",
    puesto: "Data Engineer",
    areaId: 3,
    roles: ["empleado", "formador"],
    modalidadTrabajo: "Remoto"
  },
  {
    _id: 6,
    nombre: "Hugo",
    apellidos: "Prieto Sánchez",
    telefono: "+34 600 333 302",
    puesto: "BI Analyst",
    areaId: 3,
    roles: ["empleado"],
    modalidadTrabajo: "Híbrido"
  },
  {
    _id: 7,
    nombre: "Sergio",
    apellidos: "Navarro Gómez",
    telefono: "+34 600 444 401",
    puesto: "Backend Developer",
    areaId: 4,
    roles: ["empleado"],
    modalidadTrabajo: "Presencial"
  },
  {
    _id: 8,
    nombre: "Elena",
    apellidos: "Suárez Martín",
    telefono: "+34 600 444 402",
    puesto: "Frontend Developer",
    areaId: 4,
    roles: ["empleado", "formador"],
    modalidadTrabajo: "Híbrido"
  }
])

db.cursos.insertMany([
  {
    _id: 1,
    titulo: "Introducción a Ciberseguridad",
    categoria: "Ciberseguridad",
    horas: 6,
    modalidad: "Presencial",
    formadores: [ { personaId: 1 } ],
    areaId: 1
  },
  {
    _id: 2,
    titulo: "IAM: SSO y MFA en la empresa",
    categoria: "Ciberseguridad",
    horas: 4,
    modalidad: "Online",
    formadores: [ { personaId: 1 }, { personaId: 3 } ],
    areaId: 1
  },
  {
    _id: 3,
    titulo: "Docker y contenedores",
    categoria: "DevOps",
    horas: 8,
    modalidad: "Mixto",
    formadores: [ { personaId: 8 } ],
    areaId: 2
  }
])