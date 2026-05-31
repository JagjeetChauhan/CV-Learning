import { useState } from "react";
import MatrixGrid from "./components/MatrixGrid";
import ControlPanel from "./components/ControlPanel";
import FormulaBox from "./components/FormulaBox";

function App() {

  const [inputSize, setInputSize] = useState(8);
  const [kernelSize, setKernelSize] = useState(3);
  const [padding, setPadding] = useState(0);
  const [stride, setStride] = useState(1);

  const generateMatrix = (size: number) => {
    return Array(size)
      .fill(0)
      .map(() =>
        Array(size)
          .fill(0)
          .map(() => Math.floor(Math.random() * 10))
      );
  };

  const inputMatrix = generateMatrix(inputSize);
  const kernelMatrix = generateMatrix(kernelSize);

  const outputSize =
    ((inputSize - kernelSize + 2 * padding) / stride) + 1;

  return (
    <div className="app">

      <h1>CNN Kernel Playground</h1>

      <div className="top-section">

        <ControlPanel
          inputSize={inputSize}
          setInputSize={setInputSize}
          kernelSize={kernelSize}
          setKernelSize={setKernelSize}
          padding={padding}
          setPadding={setPadding}
          stride={stride}
          setStride={setStride}
        />

        <div>
          <h2>Input Matrix</h2>
          <MatrixGrid matrix={inputMatrix} />
        </div>

      </div>

      <div className="bottom-section">

        <div>
          <h2>Kernel</h2>
          <MatrixGrid matrix={kernelMatrix} />
        </div>

        <div>
          <h2>Output Matrix</h2>
          <MatrixGrid
            matrix={Array(Math.floor(outputSize))
              .fill(0)
              .map(() =>
                Array(Math.floor(outputSize)).fill(0)
              )}
          />
        </div>

      </div>

      <FormulaBox
        inputSize={inputSize}
        kernelSize={kernelSize}
        padding={padding}
        stride={stride}
      />

    </div>
  );
}

export default App;