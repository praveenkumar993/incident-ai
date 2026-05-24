import { useState } from "react"

import { motion } from "framer-motion"
import { useDropzone } from "react-dropzone"
import LoadingScanner from "./components/LoadingScanner"


import {
  ShieldAlert,
  Activity,
  ServerCrash,
  Cpu,
  UploadCloud
} from "lucide-react"

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts"

import toast, { Toaster } from "react-hot-toast"

import { analyzeIncident } from "./services/api"

// BUG FIX 1: case-insensitive severity matching + flexible field names
const getSeverity = (log) => {
  const raw = (
    log.severity ||
    log.level ||
    log.priority ||
    ""
  ).toString().toLowerCase().trim()
  return raw
}

const calculateSeverityData = (logs) => {

  let critical = 0
  let high = 0
  let medium = 0

  logs.forEach((log) => {
    // BUG FIX 1: use getSeverity() for case-insensitive comparison
    const sev = getSeverity(log)

    if (sev === "critical" || sev === "crit" || sev === "fatal") {
      critical++
    }
    else if (sev === "high" || sev === "error" || sev === "err") {
      high++
    }
    else if (sev === "medium" || sev === "warning" || sev === "warn" || sev === "moderate") {
      medium++
    }
  })

  return [
    { name: "Critical", value: critical },
    { name: "High", value: high },
    { name: "Medium", value: medium }
  ]
}

const COLORS = ["#ef4444", "#f97316", "#eab308"]

function App() {

  const [logs, setLogs] = useState("")
  const [report, setReport] = useState("")
  const [loading, setLoading] = useState(false)
  const onDrop = (acceptedFiles) => {

  const file = acceptedFiles[0]

  const reader = new FileReader()

  reader.onload = () => {

    try {

      const parsed = JSON.parse(reader.result)

      setLogs(JSON.stringify(parsed, null, 2))

      toast.success("Incident file uploaded!")

    } catch {

      toast.error("Invalid JSON file")
    }
  }

  reader.readAsText(file)
}

const { getRootProps, getInputProps } = useDropzone({
  onDrop,
  accept: {
    "application/json": [".json"]
  }
})
  

  const handleAnalyze = async () => {

    try {

      setLoading(true)

      toast.loading("AI agents analyzing incidents...", {
        id: "analysis"
      })

      const parsedLogs = JSON.parse(logs)

      const response = await analyzeIncident(
        parsedLogs.incident_logs
      )

      setReport(response.report)

      toast.success("Incident analysis completed!", {
        id: "analysis"
      })

    } catch (error) {

      console.error(error)

      toast.error("Invalid JSON or backend error")
    }

    setLoading(false)
  }

  // BUG FIX 2: support multiple JSON shapes (incident_logs, logs, incidents, or bare array)
  let parsedData = []

  try {

    if (logs.trim()) {

      const parsed = JSON.parse(logs)

      parsedData =
        parsed.incident_logs ||
        parsed.logs ||
        parsed.incidents ||
        (Array.isArray(parsed) ? parsed : [])
    }

  } catch {

    parsedData = []
  }

  const severityData =
    calculateSeverityData(parsedData)

  const criticalCount =
    severityData.find(
      item => item.name === "Critical"
    )?.value || 0

  const highCount =
    severityData.find(
      item => item.name === "High"
    )?.value || 0

  const mediumCount =
    severityData.find(
      item => item.name === "Medium"
    )?.value || 0

  const totalIncidents =
    criticalCount +
    highCount +
    mediumCount

  // BUG FIX 3: AI Agents card was showing totalIncidents (same as Critical Alerts).
  // It should show the number of agents spawned, not the total incident count.
  const activeAgents = parsedData.length

  const systemHealth = Math.max(
    100 - (
      criticalCount * 15 +
      highCount * 10 +
      mediumCount * 5
    ),
    0
  )

  const chartData =
    severityData.filter(
      item => item.value > 0
    )

  return (

    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-black to-slate-900 text-white overflow-hidden">

      <Toaster position="top-right" />

      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,#1e293b,transparent_40%)] opacity-30" />

      <motion.div
        initial={{ opacity: 0, y: -40 }}
        animate={{ opacity: 1, y: 0 }}
        className="relative z-10 p-10"
      >

        <h1 className="text-6xl font-extrabold text-center bg-gradient-to-r from-red-500 via-orange-400 to-yellow-300 bg-clip-text text-transparent">
          Incident AI Ops Center
        </h1>

        <p className="text-center text-slate-400 mt-4 text-lg">
          Autonomous Multi-Agent Incident Intelligence Platform
        </p>

      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 px-10 relative z-10">

        <motion.div
          whileHover={{ scale: 1.03 }}
          className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-6 shadow-2xl"
        >
          <div className="flex items-center gap-3">
            <ShieldAlert className="text-red-400" size={32} />
            <h2 className="text-2xl font-bold">
              Critical Alerts
            </h2>
          </div>

          <p className="text-5xl mt-6 font-extrabold text-red-400">
            {totalIncidents}
          </p>

          <p className="text-slate-400 mt-2">
            Active incidents detected
          </p>
        </motion.div>

        <motion.div
          whileHover={{ scale: 1.03 }}
          className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-6 shadow-2xl"
        >
          <div className="flex items-center gap-3">
            <Activity className="text-green-400" size={32} />
            <h2 className="text-2xl font-bold">
              AI Agents
            </h2>
          </div>

          {/* BUG FIX 3: show activeAgents instead of duplicate totalIncidents */}
          <p className="text-5xl mt-6 font-extrabold text-green-400">
            {activeAgents}
          </p>

          <p className="text-slate-400 mt-2">
            Autonomous agents running
          </p>
        </motion.div>

        <motion.div
          whileHover={{ scale: 1.03 }}
          className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-6 shadow-2xl"
        >
          <div className="flex items-center gap-3">
            <Cpu className="text-yellow-300" size={32} />
            <h2 className="text-2xl font-bold">
              System Health
            </h2>
          </div>

          <p className="text-5xl mt-6 font-extrabold text-yellow-300">
            {systemHealth}%
          </p>

          <p className="text-slate-400 mt-2">
            Infrastructure operational
          </p>
        </motion.div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 px-10 mt-10 relative z-10">

        <motion.div
          initial={{ opacity: 0, x: -40 }}
          animate={{ opacity: 1, x: 0 }}
          className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-8 shadow-2xl"
        >

          <div className="flex items-center gap-3 mb-6">
            <UploadCloud className="text-cyan-400" size={30} />
            <h2 className="text-3xl font-bold">
              Incident Upload
            </h2>
          </div>

          <div
  {...getRootProps()}
  className="border-2 border-dashed border-cyan-500 rounded-2xl p-10 text-center cursor-pointer hover:bg-cyan-500/10 transition-all duration-300"
>

  <input {...getInputProps()} />

  <UploadCloud
    size={50}
    className="mx-auto text-cyan-400"
  />

  <p className="mt-5 text-slate-300">
    Drag & Drop logs.json here
  </p>

  <p className="text-sm text-slate-500 mt-2">
    or click to upload
  </p>

</div>

<textarea
  value={logs}
  onChange={(e) => setLogs(e.target.value)}
  className="w-full h-72 mt-6 bg-slate-900/70 border border-slate-700 rounded-2xl p-5 outline-none text-sm"
  placeholder="Paste incident logs JSON here..."
/>

          <button
            onClick={handleAnalyze}
            className="mt-6 w-full bg-gradient-to-r from-red-500 via-orange-500 to-yellow-400 py-4 rounded-2xl font-bold text-lg hover:scale-105 transition-all duration-300"
          >
            {
              loading
              ? "AI Agents Investigating..."
              : "Analyze Incident"
            }
          </button>

        </motion.div>

        <motion.div
          initial={{ opacity: 0, x: 40 }}
          animate={{ opacity: 1, x: 0 }}
          className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-8 shadow-2xl"
        >

          <div className="flex items-center gap-3 mb-6">
            <ServerCrash className="text-pink-400" size={30} />
            <h2 className="text-3xl font-bold">
              Incident Severity
            </h2>
          </div>

          <div className="h-80">

            <ResponsiveContainer width="100%" height="100%">
              <PieChart>

                <Pie
                  data={chartData}
                  dataKey="value"
                  outerRadius={120}
                  innerRadius={60}
                  paddingAngle={5}
                  label
                >

                  {
                    chartData.map((entry, index) => (
                      <Cell
                        key={index}
                        fill={COLORS[index % COLORS.length]}
                      />
                    ))
                  }

                </Pie>

                <Tooltip />

              </PieChart>
            </ResponsiveContainer>

          </div>

        </motion.div>

      </div>
      {
        loading && (
          <LoadingScanner />
        )
      }

      {
        report && (

          <motion.div
            initial={{ opacity: 0, y: 60 }}
            animate={{ opacity: 1, y: 0 }}
            className="mx-10 mt-10 mb-20 bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-8 shadow-2xl relative z-10"
          >

            <h2 className="text-4xl font-bold mb-8 bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
              AI Incident Intelligence Report
            </h2>

            <pre className="whitespace-pre-wrap text-sm leading-8 text-slate-200">
              {report}
            </pre>

          </motion.div>
        )
      }

    </div>
  )
}

export default App
