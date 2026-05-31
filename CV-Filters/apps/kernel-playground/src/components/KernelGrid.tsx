type Props = {
  kernel:number[][];
};

function KernelGrid({kernel}:Props){

  return (

    <div className="grid">

      {kernel.map((row,rowIndex)=>

        row.map((value,colIndex)=>(

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

export default KernelGrid;