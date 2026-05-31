type Props = {
  matrix: number[][];
};

function MatrixGrid({ matrix }: Props) {

  const cols = matrix[0]?.length || 1;

  return (
    <div
      className="grid"
      style={{
        gridTemplateColumns: `repeat(${cols}, 40px)`
      }}
    >
      {matrix.map((row, rowIndex) =>
        row.map((value, colIndex) => (
          <div
            key={`${rowIndex}-${colIndex}`}
            className="cell"
          >
            {value}
          </div>
        ))
      )}
    </div>
  );
}

export default MatrixGrid;