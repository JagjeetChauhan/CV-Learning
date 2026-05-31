type Props = {
  inputSize: number;
  setInputSize: React.Dispatch<React.SetStateAction<number>>;

  kernelSize: number;
  setKernelSize: React.Dispatch<React.SetStateAction<number>>;

  padding: number;
  setPadding: React.Dispatch<React.SetStateAction<number>>;

  stride: number;
  setStride: React.Dispatch<React.SetStateAction<number>>;
};

function ControlPanel({
  inputSize,
  setInputSize,
  kernelSize,
  setKernelSize,
  padding,
  setPadding,
  stride,
  setStride
}: Props) {

  return (
    <div className="control-panel">

      <h2>Controls</h2>

      <label>
        Input Size: {inputSize}
      </label>

      <input
        type="range"
        min="4"
        max="12"
        value={inputSize}
        onChange={(e) =>
          setInputSize(Number(e.target.value))
        }
      />

      <label>
        Kernel Size: {kernelSize}
      </label>

      <input
        type="range"
        min="1"
        max="7"
        step="2"
        value={kernelSize}
        onChange={(e) =>
          setKernelSize(Number(e.target.value))
        }
      />

      <label>
        Padding: {padding}
      </label>

      <input
        type="range"
        min="0"
        max="5"
        value={padding}
        onChange={(e) =>
          setPadding(Number(e.target.value))
        }
      />

      <label>
        Stride: {stride}
      </label>

      <input
        type="range"
        min="1"
        max="5"
        value={stride}
        onChange={(e) =>
          setStride(Number(e.target.value))
        }
      />

    </div>
  );
}

export default ControlPanel;