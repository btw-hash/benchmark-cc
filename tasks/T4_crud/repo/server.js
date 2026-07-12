import express from 'express';

const app = express();
app.use(express.json());

// In-memory store
const users = new Map();
let nextId = 1;

app.post('/users', (req, res) => {
  const { name, email } = req.body ?? {};
  if (!name || !email) return res.status(400).json({ error: 'name and email required' });
  const id = String(nextId++);
  const user = { id, name, email };
  users.set(id, user);
  res.status(201).json(user);
});

app.get('/users/:id', (req, res) => {
  const u = users.get(req.params.id);
  if (!u) return res.status(404).json({ error: 'not found' });
  res.json(u);
});

app.delete('/users/:id', (req, res) => {
  if (!users.has(req.params.id)) return res.status(404).json({ error: 'not found' });
  users.delete(req.params.id);
  res.status(204).end();
});

// TODO: implement PATCH /users/:id

export default app;
export { users };
