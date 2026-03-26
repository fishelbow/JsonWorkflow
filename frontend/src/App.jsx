import React, { useState } from 'react';
import ReactFlow, { 
  Background, 
  Controls, 
  applyNodeChanges, 
  applyEdgeChanges 
} from 'reactflow';
import 'reactflow/dist/style.css';

export default function App() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);
  const [selectedNode, setSelectedNode] = useState(null);
  const [warning, setWarning] = useState('');

  // Add a new task node
  function addNode() {
    setNodes((nds) => [
      ...nds,
      {
        id: crypto.randomUUID(),
        position: { x: 200, y: 200 },
        data: { 
          label: 'New Task',
          taskType: 'print',
          message: ''
        }
      }
    ]);
  }

  // Delete the currently selected node
  function deleteNode() {
    if (!selectedNode) return;

    setNodes((nds) => nds.filter((n) => n.id !== selectedNode.id));
    setEdges((eds) =>
      eds.filter(
        (e) => e.source !== selectedNode.id && e.target !== selectedNode.id
      )
    );

    setSelectedNode(null);
  }

  // Track which node is selected
  function onSelectionChange({ nodes }) {
    setSelectedNode(nodes[0] || null);
  }

  // --- Cycle Detection Helper ---
  function createsCycle(source, target, edges) {
    const graph = {};

    // Build adjacency list
    edges.forEach((e) => {
      if (!graph[e.source]) graph[e.source] = [];
      graph[e.source].push(e.target);
    });

    // Add the new edge temporarily
    if (!graph[source]) graph[source] = [];
    graph[source].push(target);

    // DFS to detect cycle
    const visited = new Set();

    function dfs(node) {
      if (node === source) return true; // cycle found
      if (visited.has(node)) return false;
      visited.add(node);

      const neighbors = graph[node] || [];
      for (let n of neighbors) {
        if (dfs(n)) return true;
      }
      return false;
    }

    return dfs(target);
  }

  // --- Safe Connect Handler ---
function onConnect(connection) {
  const { source, target } = connection;

  if (createsCycle(source, target, edges)) {
    setWarning(`Cannot connect these nodes, this would create a cycle.`);

    // Auto-hide after 2 seconds
    setTimeout(() => {
      setWarning('');
    }, 2000);

    return;
  }

  setWarning('');
  setEdges((eds) => [...eds, connection]);
}

  return (
    <div style={{ width: '100vw', height: '100vh' }}>

      {/* Add Task Button */}
      <button
        onClick={addNode}
        style={{
          position: 'absolute',
          zIndex: 10,
          left: 20,
          top: 20,
          padding: '8px 12px'
        }}
      >
        Add Task
      </button>

      {/* Delete Task Button */}
      <button
        onClick={deleteNode}
        style={{
          position: 'absolute',
          zIndex: 10,
          left: 120,
          top: 20,
          padding: '8px 12px'
        }}
      >
        Delete Task
      </button>

      {/* Warning Message */}
      {warning && (
        <div
          style={{
            position: 'absolute',
            top: 60,
            left: 20,
            zIndex: 10,
            padding: '8px 12px',
            background: '#ffdddd',
            border: '1px solid #ff8888',
            borderRadius: '4px'
          }}
        >
          {warning}
        </div>
      )}

      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={(changes) =>
          setNodes((nds) => applyNodeChanges(changes, nds))
        }
        onEdgesChange={(changes) =>
          setEdges((eds) => applyEdgeChanges(changes, eds))
        }
        onConnect={onConnect}
        onSelectionChange={onSelectionChange}
      >
        <Background color="#aaa" gap={16} />
        <Controls />
      </ReactFlow>
    </div>
  );
}