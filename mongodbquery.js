// MongoDB Read Operation

//_______________________________________________
// Find all documents in 'users' collection

db.users.find()

//________________________________________________
// Find first 5 document in collection 'users'.

db.users.find(
   { role: "teammember" }, 
   { fname: 1, lname: 1 } 
).limit(5)

//________________________________________________
db.users.find( 
   { role: {$gt: "a" }, {_id: 0} }, 
)sort( {role: 1} )

//________________________________________________

// MongoDB Write Operations

//________________________________________________

db.users.insert(
   {
     login: 'olav',
     pass: 'passpass',
     fname: 'Omar',
     lname: 'La Vei'
     role: admin
     todolist: []
     assignto: []
   }
)

// Update
db.users.update(
   { login: "pharis" },
   { $set: { pass: "pasharis"} }
)



db.users.update({ login: "pharis" }, { $set: { pass: "pasharis"} })

