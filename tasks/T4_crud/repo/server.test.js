import { describe, it, expect, beforeEach } from 'vitest';
import request from 'supertest';
import app, { users } from './server.js';

beforeEach(() => {
  users.clear();
});

async function createUser(name = 'Alice', email = 'a@x.com') {
  const r = await request(app).post('/users').send({ name, email });
  return r.body;
}

describe('PATCH /users/:id', () => {
  it('updates name only', async () => {
    const u = await createUser('Alice', 'a@x.com');
    const r = await request(app).patch(`/users/${u.id}`).send({ name: 'Alicia' });
    expect(r.status).toBe(200);
    expect(r.body).toEqual({ id: u.id, name: 'Alicia', email: 'a@x.com' });
  });

  it('updates email only', async () => {
    const u = await createUser();
    const r = await request(app).patch(`/users/${u.id}`).send({ email: 'new@x.com' });
    expect(r.status).toBe(200);
    expect(r.body.email).toBe('new@x.com');
    expect(r.body.name).toBe('Alice');
  });

  it('updates both', async () => {
    const u = await createUser();
    const r = await request(app).patch(`/users/${u.id}`).send({ name: 'N', email: 'e@x.com' });
    expect(r.status).toBe(200);
    expect(r.body).toEqual({ id: u.id, name: 'N', email: 'e@x.com' });
  });

  it('404 for missing user', async () => {
    const r = await request(app).patch('/users/999').send({ name: 'X' });
    expect(r.status).toBe(404);
  });

  it('rejects empty body', async () => {
    const u = await createUser();
    const r = await request(app).patch(`/users/${u.id}`).send({});
    expect(r.status).toBe(400);
  });

  it('rejects unknown fields', async () => {
    const u = await createUser();
    const r = await request(app).patch(`/users/${u.id}`).send({ admin: true });
    expect(r.status).toBe(400);
  });

  it('does not change id', async () => {
    const u = await createUser();
    const r = await request(app).patch(`/users/${u.id}`).send({ id: '999', name: 'N' });
    expect(r.status).toBe(200);
    expect(r.body.id).toBe(u.id);
  });
});
