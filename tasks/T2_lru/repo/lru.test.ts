import { describe, it, expect } from 'vitest';
import { LRUCache } from './lru';

describe('LRUCache', () => {
  it('returns undefined for missing keys', () => {
    const c = new LRUCache<string, number>(2);
    expect(c.get('nope')).toBeUndefined();
  });

  it('stores and retrieves', () => {
    const c = new LRUCache<string, number>(2);
    c.put('a', 1);
    c.put('b', 2);
    expect(c.get('a')).toBe(1);
    expect(c.get('b')).toBe(2);
  });

  it('evicts least-recently-used', () => {
    const c = new LRUCache<string, number>(2);
    c.put('a', 1);
    c.put('b', 2);
    c.put('c', 3); // evicts "a"
    expect(c.get('a')).toBeUndefined();
    expect(c.get('b')).toBe(2);
    expect(c.get('c')).toBe(3);
  });

  it('get() refreshes recency', () => {
    const c = new LRUCache<string, number>(2);
    c.put('a', 1);
    c.put('b', 2);
    c.get('a'); // "a" now most-recent
    c.put('c', 3); // evicts "b", not "a"
    expect(c.get('a')).toBe(1);
    expect(c.get('b')).toBeUndefined();
    expect(c.get('c')).toBe(3);
  });

  it('put() updates value and refreshes recency', () => {
    const c = new LRUCache<string, number>(2);
    c.put('a', 1);
    c.put('b', 2);
    c.put('a', 100); // update
    c.put('c', 3); // evicts "b"
    expect(c.get('a')).toBe(100);
    expect(c.get('b')).toBeUndefined();
    expect(c.get('c')).toBe(3);
  });

  it('handles capacity 1', () => {
    const c = new LRUCache<string, number>(1);
    c.put('a', 1);
    c.put('b', 2);
    expect(c.get('a')).toBeUndefined();
    expect(c.get('b')).toBe(2);
  });
});
