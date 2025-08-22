export default class Currency {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof value !== 'integer') {
      throw new TypeError('Code must be a number');
    }
    this._size = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Location must be a string');
    }
    this._location = value;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}