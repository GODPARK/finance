package com.finance.data.repository;

import com.finance.data.entity.USStock;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface USStockRepository extends JpaRepository<USStock, Long> {
}
