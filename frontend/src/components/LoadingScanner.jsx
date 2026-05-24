import { motion } from "framer-motion"

function LoadingScanner() {

  return (

    <div className="flex flex-col items-center justify-center py-20">

      <motion.div
        animate={{
          rotate: 360
        }}
        transition={{
          repeat: Infinity,
          duration: 2,
          ease: "linear"
        }}
        className="w-32 h-32 rounded-full border-4 border-red-500 border-t-transparent"
      />

      <motion.p
        animate={{
          opacity: [0.3, 1, 0.3]
        }}
        transition={{
          repeat: Infinity,
          duration: 1.5
        }}
        className="mt-10 text-xl font-bold text-red-400 tracking-widest"
      >
        AI AGENTS INVESTIGATING INCIDENTS...
      </motion.p>

    </div>
  )
}

export default LoadingScanner