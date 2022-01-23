import glob
from tools import get_all_Pk, get_all_red_Pk, get_mat_Pk, write_asdf, get_Pk_splits, get_all_cf

# parameters
Lbox = 2000. # Mpc/h
N_dim = 2304
interlaced = True
redshifts = [0.1, 0.3, 0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.5, 3.0]
sim_name = "AbacusSummit_base_c000_ph006"

header = {}
header['Lbox'] = Lbox
header['N_dim'] = N_dim
header['sim_name'] = sim_name
header['interlaced'] = interlaced
header['units'] = 'Mpc/h'

for redshift in redshifts:
    header['redshift'] = redshift

    # filenames
    pos_halo_1_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_1.fits"
    pos_halo_2_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_2.fits"
    pos_halo_3_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_3.fits"

    pos_halo_1_s1_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_1_1sthalf.fits"
    pos_halo_1_s2_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_1_2ndhalf.fits"
    pos_halo_2_s1_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_2_1sthalf.fits"
    pos_halo_2_s2_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_2_2ndhalf.fits"
    pos_halo_3_s1_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_3_1sthalf.fits"
    pos_halo_3_s2_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_halo/{sim_name:s}/z{redshift:.3f}/halos/pos_halo_3_2ndhalf.fits"

    pos_gal_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_red_AB/{sim_name:s}/z{redshift:.3f}/galaxies/pos_red_AB_galaxy.fits"
    pos_gal_red_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_red/{sim_name:s}/z{redshift:.3f}/galaxies/pos_red_galaxy.fits"
    pos_gal_all_fns = f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks/{sim_name:s}/z{redshift:.3f}/galaxies/pos_all_galaxy.fits"
    pos_mat_fns = sorted(glob.glob(f"/global/cscratch1/sd/boryanah/AbacusHOD_David_scratch/mocks_red/{sim_name:s}/z{redshift:.3f}/matter/pos_matter_*.fits"))
    dens_dir = f"/global/cscratch1/sd/boryanah/data_hybrid/abacus/{sim_name:s}/"
    data_dir = "/global/homes/b/boryanah/lsst_bias/data/"
    data_dir = "/global/homes/a/anicola/output/"
    
    # save all power spectra
    # matter
    # power_mat_dic = get_mat_Pk(pos_mat_fns, dens_dir, data_dir, N_dim, Lbox, interlaced, dk=None)
    # write_asdf(power_mat_dic, (f"power_mat_z{redshift:.3f}.asdf"), data_dir, header=header)
    #
    # # galaxies and matter
    # power_all_dic, power_red_dic = get_all_red_Pk(pos_gal_all_fns, pos_gal_red_fns, pos_mat_fns, dens_dir, data_dir, N_dim, Lbox, interlaced, dk=None)
    #
    # header['gal_sample'] = 'all'
    # write_asdf(power_all_dic, (f"power_all_z{redshift:.3f}.asdf"), data_dir, header=header)
    #
    # header['gal_sample'] = 'red'
    # write_asdf(power_red_dic, (f"power_red_z{redshift:.3f}.asdf"), data_dir, header=header)
    #
    # power_dic = get_all_Pk(pos_gal_fns, pos_mat_fns, dens_dir, data_dir, N_dim, Lbox, interlaced, dk=None)
    # header['gal_sample'] = 'red_AB'
    # write_asdf(power_dic, (f"power_red_AB_z{redshift:.3f}.asdf"), data_dir, header=header)
    #
    cf_dic = get_all_cf(pos_halo_1_fns, pos_mat_fns, Lbox)
    header['gal_sample'] = 'halo_12.0_12.5'
    write_asdf(cf_dic, (f"cf_halo_1_z{redshift:.3f}.asdf"), data_dir, header=header)

    cf_dic = get_all_cf(pos_halo_2_fns, pos_mat_fns, Lbox)
    header['gal_sample'] = 'halo_12.5_13.0'
    write_asdf(cf_dic, (f"cf_halo_2_z{redshift:.3f}.asdf"), data_dir, header=header)

    cf_dic = get_all_cf(pos_halo_3_fns, pos_mat_fns, Lbox)
    header['gal_sample'] = 'halo_13.0_13.5'
    write_asdf(cf_dic, (f"cf_halo_3_z{redshift:.3f}.asdf"), data_dir, header=header)

    # power_dic = get_Pk_splits(pos_halo_1_s1_fns, pos_halo_1_s2_fns, pos_mat_fns, N_dim, Lbox, interlaced, dk=None)
    # header['gal_sample'] = 'halo_splits_12.0_12.5'
    # write_asdf(power_dic, (f"power_halo_1_splits_z{redshift:.3f}.asdf"), data_dir, header=header)
    #
    # power_dic = get_Pk_splits(pos_halo_2_s1_fns, pos_halo_2_s2_fns, pos_mat_fns, N_dim, Lbox, interlaced, dk=None)
    # header['gal_sample'] = 'halo_splits_12.5_13.0'
    # write_asdf(power_dic, (f"power_halo_2_splits_z{redshift:.3f}.asdf"), data_dir, header=header)
    #
    # power_dic = get_Pk_splits(pos_halo_3_s1_fns, pos_halo_3_s2_fns, pos_mat_fns, N_dim, Lbox, interlaced, dk=None)
    # header['gal_sample'] = 'halo_splits_13.0_13.5'
    # write_asdf(power_dic, (f"power_halo_3_splits_z{redshift:.3f}.asdf"), data_dir, header=header)
