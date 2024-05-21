const createInt8TypedArray = (length, position, value) => {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  try {
    view.setInt8(position, value);
  } catch (err) {
    throw new Error('Position outside range');
  }

  return new Int8Array(buffer);
};

export default createInt8TypedArray;
