package com.finance.data.repository;

import com.finance.data.entity.BaseRate;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BaseRateRepository extends JpaRepository<BaseRate, Long> {
}
