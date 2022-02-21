
# mtxName = ["Queen_4147"]
mtxName = [
    "Queen_4147",
    "Bump_2911",
    "G3_circuit",
    "Flan_1565",
    "Hook_1498",
    "StocF-1465",
    "Geo_1438",
    "Serena",
    "thermal2",
    "ecology2",
    "bone010",
    "ldoor",
    "audikw_1",
    "Emilia_923",
    "boneS10",
    "PFlow_742",
    "tmt_sym",
    "apache2",
    "Fault_639",
    "parabolic_fem",
    "bundle_adj",
    "af_shell8",
    "af_shell4",
    "af_shell3",
    "af_shell7",
    "inline_1",
    "af_0_k101",
    "af_4_k101",
    "af_3_k101",
    "af_2_k101"
]

rmMtx = []
# rmMtx = [
#     "awdikw_1",
#     "boneS10",
#     "Bump_2911",
#     "bundle_adj",
#     "Fault_639",
#     "ldoor",
#     "PFlow_742",
#     "Queen_4147",
#     "Serena",
#     "StocF-1465",
#     "tmt_sym"
# ]

f = open("graph.txt", "w")

for m in mtxName:
    #     if m in rmMtx:
    #         print("\
    # \\begin{figure*}[t]\n\
    #     \\begin{center}\n\
    #     \subfloat[SC前処理（thread=40）]\n\
    #     {\n\
    #         \includegraphics[width=0.50\linewidth]{./figures/parallel/", m, ".sciccg.eps}\hspace{1cm}\n\
    #         \label{fig:parallel.", m, ".sciccg}\n\
    #     }\n\
    #     \subfloat[Deflation（thread=40）]\n\
    #     {\n\
    #         \includegraphics[width=0.50\linewidth]{./figures/parallel/", m, ".diccg.eps}\n\
    #         \label{fig:parallel.", m, ".diccg}\n\
    #     }\n\
    #     \end{center}\n\
    #     \caption{", "\_".join(m.split("_")), "の収束履歴}\n\
    #     \label{fig:", m, "}\n\
    # \end{figure*}\n\
    #     ", sep="")

    #     else:
    if m not in rmMtx:
        print("\
    \\begin{figure*}[htp]\n\
    \\begin{center}\n\
    \\subfloat[b=1.thread=1]\n\
    {\n\
        \\includegraphics[width=0.38\linewidth]{eps/", m, ".b=1.thread=1.eps}\n\
        \\label{fig:eps.", m, ".b=1.thread=1}\n\
    }\n\
    \\subfloat[b=1.thread=40]\n\
    {\n\
        \\includegraphics[width=0.38\linewidth]{eps/", m, ".b=1.thread=40.eps}\n\
        \\label{fig:eps.", m, ".b=1.thread=40}\n\
    }\n\
    \\hfill\n\
    \\subfloat[b=rand.thread=1]\n\
    {\n\
        \\includegraphics[width=0.38\linewidth]{eps/", m, ".b=rand.thread=1.eps}\n\
        \\label{fig:eps.", m, ".b=rand.thread=1}\n\
    }\n\
    \\subfloat[b=rand.thread=40]\n\
    {\n\
        \\includegraphics[width=0.38\linewidth]{eps/", m, ".b=rand.thread=40.eps}\n\
        \\label{fig:eps.", m, ".b=rand.thread=40}\n\
    }\n\
    \\end{center}\n\
    \\caption{", m, "}\n\
    \\label{fig:", m, "}\n\
\\end{figure*}\n\
        ", sep="", file=f)
