// Implement an LRU (Least Recently Used) cache with O(1) get and put.
//
// Constructor takes a positive integer capacity.
// `get(key)`: returns the value, or undefined if absent. Counts as a "use".
// `put(key, value)`: inserts or updates. Evicts the least-recently-used entry
//   when capacity would be exceeded.
//
// Both operations must run in O(1) amortized time. Use a Map + doubly linked list
// (or any other approach that meets the complexity requirement).

export class LRUCache<K, V> {
  constructor(capacity: number) {
    throw new Error('not implemented');
  }
  get(key: K): V | undefined {
    throw new Error('not implemented');
  }
  put(key: K, value: V): void {
    throw new Error('not implemented');
  }
}
