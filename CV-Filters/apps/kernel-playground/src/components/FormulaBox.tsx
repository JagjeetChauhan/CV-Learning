type Props = {
  inputSize: number;
  kernelSize: number;
  padding: number;
  stride: number;
};

function FormulaBox({
  inputSize,
  kernelSize,
  padding,
  stride
}: Props) {

  const output =
    ((inputSize - kernelSize + 2 * padding) / stride) + 1;

  return (
    <div className="formula-box">

      <h2>Output Size Formula</h2>

      <p>
        ({inputSize} - {kernelSize} + 2×{padding})
        /
        {stride}
        + 1
      </p>

      <h3>
        Output Size = {output}
      </h3>

    </div>
  );
}

export default FormulaBox;