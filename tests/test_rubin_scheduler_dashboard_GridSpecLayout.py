import numpy as np

from schedview.dashboards.rubin_scheduler_dashboard_GridSpecLayout import (generate_array_for_key,
                                                                           Scheduler,
                                                                           )


def test_letsgo():
    assert 1 == 1

def test_generate_array_for_key():
    
    data = generate_array_for_key()
    
    assert np.array_equal(data["text_1"], ['Horizon','ZD=70 degrees','Ecliptic','Galactic plane'])
    assert np.array_equal(data["text_2"], ['Sun position','Moon position','Survey field(s)','Telescope pointing'])
    
    # ALTERNATIVE: concatenate all values for all keys into a giant array and then check if "Horizon" in array.
    

def test_scheduler_class():
    
    scheduler = Scheduler()
    
    scheduler._scheduler = 'random'
    scheduler.param["tier"].objects = ['tier 1']
    scheduler.tier = 'tier 1'
    scheduler._plot_display = 1
    scheduler.basis_function = 0
    
    assert scheduler.generate_dashboard_title() == '\nTier 1 - Survey 0 - Map '
    
    scheduler._plot_display = 2
    scheduler.basis_function = 1
    
    assert scheduler.generate_dashboard_title() == '\nTier 1 - Survey 0 - Basis function 1'
    
    # Check if map is not in the string

# to test non-returning function, check for side-effects.

# where lines such as (scheduler, conditions) = schedview.collect.scheduler_pickle.read_scheduler(self.scheduler_fname) 
# use a mock test