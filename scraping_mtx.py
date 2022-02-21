table = ["Queen_4147	Janna	4,147,110	4,147,110	316,548,962	2D/3D Problem",
         "Bump_2911	Janna	2,911,419	2,911,419	127,729,899	2D/3D Problem",
         "G3_circuit	AMD	1,585,478	1,585,478	7,660,826	Circuit Simulation Problem",
         "Flan_1565	Janna	1,564,794	1,564,794	114,165,372	Structural Problem",
         "Hook_1498	Janna	1,498,023	1,498,023	59,374,451	Structural Problem",
         "StocF-1465	Janna	1,465,137	1,465,137	21,005,389	Computational Fluid Dynamics Problem",
         "Geo_1438	Janna	1,437,960	1,437,960	60,236,322	Structural Problem",
         "Serena	Janna	1,391,349	1,391,349	64,131,971	Structural Problem",
         "thermal2	Schmid	1,228,045	1,228,045	8,580,313	Thermal Problem",
         "ecology2	McRae	999,999	999,999	4,995,991	2D/3D Problem",
         "bone010	Oberwolfach	986,703	986,703	47,851,783	Model Reduction Problem",
         "ldoor	GHS_psdef	952,203	952,203	42,493,817	Structural Problem",
         "audikw_1	GHS_psdef	943,695	943,695	77,651,847	Structural Problem",
         "Emilia_923	Janna	923,136	923,136	40,373,538	Structural Problem",
         "boneS10	Oberwolfach	914,898	914,898	40,878,708	Model Reduction Problem",
         "PFlow_742	Janna	742,793	742,793	37,138,461	2D/3D Problem",
         "tmt_sym	CEMW	726,713	726,713	5,080,961	Electromagnetics Problem",
         "apache2	GHS_psdef	715,176	715,176	4,817,870	Structural Problem",
         "Fault_639	Janna	638,802	638,802	27,245,944	Structural Problem",
         "parabolic_fem	Wissgott	525,825	525,825	3,674,625	Computational Fluid Dynamics Problem",
         "bundle_adj	Mazaheri	513,351	513,351	20,207,907	Computer Vision Problem",
         "af_shell3	Schenk_AFE	504,855	504,855	17,562,051	Subsequent Structural Problem",
         "af_shell4	Schenk_AFE	504,855	504,855	17,562,051	Subsequent Structural Problem",
         "af_shell7	Schenk_AFE	504,855	504,855	17,579,155	Subsequent Structural Problem",
         "af_shell8	Schenk_AFE	504,855	504,855	17,579,155	Subsequent Structural Problem",
         "inline_1	GHS_psdef	503,712	503,712	36,816,170	Structural Problem",
         "af_3_k101	Schenk_AFE	503,625	503,625	17,550,675	Structural Problem",
         "af_0_k101	Schenk_AFE	503,625	503,625	17,550,675	Structural Problem",
         "af_4_k101	Schenk_AFE	503,625	503,625	17,550,675	Structural Problem",
         "af_1_k101	Schenk_AFE	503,625	503,625	17,550,675	Structural Problem",
         "af_2_k101	Schenk_AFE	503,625	503,625	17,550,675	Structural Problem"]

for t in table:
    data = t.split("\t")
    name = data[0]
    n = data[2]
    nonzeros = data[4]
    kind = data[5]
    print(" ", name, "&", n, "&", nonzeros, "&", kind, "\\\\ \hline")
